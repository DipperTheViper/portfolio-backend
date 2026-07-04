from src.models.dtos.admin.repository.admin_repository_interface_dtos import (
    CreateAdminCommandDTO, CreateAdminResponseDTO, GetAdminQueryDTO, GetAdminByUsernameQueryDTO, GetAdminResponseDTO, UpdateAdminCommandDTO, DeleteAdminCommandDTO, SearchAdminQueryDTO, SearchAdminResponseDTO
)
from src.repositories.admin.adapters.admin_postgres_adapter import AdminPostgresAdapter


class AdminRepository:
    def __init__(self, postgres_adapter: AdminPostgresAdapter):
        self._postgres_adapter: AdminPostgresAdapter = postgres_adapter

    async def create_admin(self, input_dto: CreateAdminCommandDTO) -> CreateAdminResponseDTO:
        return await self._postgres_adapter.create_admin(input_dto=input_dto)

    async def get_admin(self, input_dto: GetAdminQueryDTO) -> GetAdminResponseDTO:
        return await self._postgres_adapter.get_admin(input_dto=input_dto)

    async def get_admin_by_username(self, input_dto: GetAdminByUsernameQueryDTO) -> GetAdminResponseDTO:
        return await self._postgres_adapter.get_admin_by_username(input_dto=input_dto)

    async def search_admins(self, input_dto: SearchAdminQueryDTO) -> SearchAdminResponseDTO:
        return await self._postgres_adapter.search_admins(input_dto=input_dto)

    async def update_admin(self, input_dto: UpdateAdminCommandDTO) -> None:
        await self._postgres_adapter.update_admin(input_dto=input_dto)

    async def delete_admin(self, input_dto: DeleteAdminCommandDTO) -> None:
        await self._postgres_adapter.delete_admin(input_dto=input_dto)

