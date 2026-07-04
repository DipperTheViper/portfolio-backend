from pathlib import Path

from archipy.helpers.decorators.sqlalchemy_atomic import async_postgres_sqlalchemy_atomic_decorator

from src.models.dtos.file.domain.v1.file_domain_interface_dtos import (
    CreateFileInputDTOV1,
    CreateFileOutputDTOV1,
    DeleteFileInputDTOV1,
    GetFileInputDTOV1,
    SearchFileOutputDTOV1,
    UpdateFileInputDTOV1,
)
from src.models.dtos.file.repository.file_repository_interface_dtos import (
    CreateFileResponseDTO,
    SearchFileResponseDTO,
)
from src.repositories.file.file_repository import FileRepository


class FileLogic:
    def __init__(
        self,
        repository: FileRepository,
    ) -> None:
        self._repository: FileRepository = repository

    @async_postgres_sqlalchemy_atomic_decorator
    async def create_file(self, input_dto: CreateFileInputDTOV1) -> CreateFileOutputDTOV1:
        response: CreateFileResponseDTO = await self._repository.create_file(
            file_name=input_dto.file_name,
            content=input_dto.content,
            purpose_type=input_dto.purpose_type,
        )
        return CreateFileOutputDTOV1.model_validate(obj=response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def search_files(self) -> SearchFileOutputDTOV1:
        response: SearchFileResponseDTO = await self._repository.search_files()
        return SearchFileOutputDTOV1.model_validate(response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def update_file(self, input_dto: UpdateFileInputDTOV1) -> None:
        await self._repository.update_file(
            file_uuid=input_dto.file_uuid,
            file_name=input_dto.file_name,
            content=input_dto.content,
        )

    @async_postgres_sqlalchemy_atomic_decorator
    async def delete_file(self, input_dto: DeleteFileInputDTOV1) -> None:
        await self._repository.delete_file(file_uuid=input_dto.file_uuid)

    @async_postgres_sqlalchemy_atomic_decorator
    async def get_download_target(self, input_dto: GetFileInputDTOV1) -> tuple[Path, str]:
        return await self._repository.get_download_target(file_uuid=input_dto.file_uuid)
