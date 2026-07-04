from pathlib import Path
from uuid import UUID

from src.models.dtos.file.repository.file_repository_interface_dtos import (
    CreateFileCommandDTO,
    CreateFileResponseDTO,
    DeleteFileCommandDTO,
    GetFileQueryDTO,
    GetFileResponseDTO,
    SearchFileResponseDTO,
    UpdateFileCommandDTO,
)
from src.models.types.enums import FilePurposeType, FileType
from src.repositories.file.adapters.file_postgres_adapter import FilePostgresAdapter
from src.repositories.file.adapters.file_storage_adapter import FileStorageAdapter


class FileRepository:
    def __init__(self, postgres_adapter: FilePostgresAdapter, storage_adapter: FileStorageAdapter) -> None:
        self._postgres_adapter: FilePostgresAdapter = postgres_adapter
        self._storage_adapter: FileStorageAdapter = storage_adapter

    async def create_file(
        self,
        file_name: str,
        content: bytes,
        purpose_type: FilePurposeType,
    ) -> CreateFileResponseDTO:
        stored_name = self._storage_adapter.save_file(content=content, file_name=file_name, purpose_type=purpose_type)

        try:
            command = CreateFileCommandDTO(
                file_name=file_name,
                path=stored_name,
                file_type=FileType.DOCUMENT.value,
                purpose_type=purpose_type.value,
            )
            return await self._postgres_adapter.create_file(input_dto=command)
        except Exception:
            self._storage_adapter.delete_file(stored_name)
            raise

    async def get_file(self, input_dto: GetFileQueryDTO) -> GetFileResponseDTO:
        return await self._postgres_adapter.get_file(input_dto=input_dto)

    async def search_files(self) -> SearchFileResponseDTO:
        return await self._postgres_adapter.search_files()

    async def update_file(self, file_uuid: UUID, file_name: str, content: bytes) -> None:
        existing: GetFileResponseDTO = await self._postgres_adapter.get_file(
            input_dto=GetFileQueryDTO(file_uuid=file_uuid),
        )
        purpose_type = FilePurposeType(existing.purpose_type)
        stored_name = self._storage_adapter.save_file(content=content, file_name=file_name, purpose_type=purpose_type)

        try:
            command = UpdateFileCommandDTO(file_uuid=file_uuid, file_name=file_name, path=stored_name)
            await self._postgres_adapter.update_file(input_dto=command)
        except Exception:
            self._storage_adapter.delete_file(stored_name)
            raise

        self._storage_adapter.delete_file(existing.path)

    async def delete_file(self, file_uuid: UUID) -> None:
        existing: GetFileResponseDTO = await self._postgres_adapter.get_file(
            input_dto=GetFileQueryDTO(file_uuid=file_uuid),
        )
        await self._postgres_adapter.delete_file(input_dto=DeleteFileCommandDTO(file_uuid=file_uuid))
        self._storage_adapter.delete_file(existing.path)

    async def get_download_target(self, file_uuid: UUID) -> tuple[Path, str]:
        existing: GetFileResponseDTO = await self._postgres_adapter.get_file(
            input_dto=GetFileQueryDTO(file_uuid=file_uuid),
        )
        return self._storage_adapter.get_file_path(existing.path), existing.file_name
