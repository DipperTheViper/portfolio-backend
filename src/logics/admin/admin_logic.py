from archipy.helpers.decorators.sqlalchemy_atomic import async_postgres_sqlalchemy_atomic_decorator
from uuid import UUID

from src.models.dtos.admin.domain.v1.admin_domain_interface_dtos import (
    CreateAdminInputDTOV1, CreateAdminOutputDTOV1, GetAdminInputDTOV1, GetAdminByUsernameInputDTOV1, GetAdminOutputDTOV1, UpdateAdminInputDTOV1, DeleteAdminInputDTOV1, SearchAdminInputDTOV1, SearchAdminOutputDTOV1
)
from src.models.dtos.admin.repository.admin_repository_interface_dtos import (
    CreateAdminCommandDTO, CreateAdminResponseDTO, GetAdminQueryDTO, GetAdminByUsernameQueryDTO, GetAdminResponseDTO, UpdateAdminCommandDTO, DeleteAdminCommandDTO, SearchAdminQueryDTO, SearchAdminResponseDTO
)
from src.repositories.admin.admin_repository import AdminRepository


class AdminLogic:
    def __init__(
        self,
        repository: AdminRepository,
    ) -> None:
        self._repository: AdminRepository = repository

    @async_postgres_sqlalchemy_atomic_decorator
    async def create_admin(self, input_dto: CreateAdminInputDTOV1) -> CreateAdminOutputDTOV1:
        command = CreateAdminCommandDTO.model_validate(input_dto)
        response: CreateAdminResponseDTO = await self._repository.create_admin(input_dto=command)
        return CreateAdminOutputDTOV1.model_validate(obj=response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def get_admin(self, input_dto: GetAdminInputDTOV1) -> GetAdminOutputDTOV1:
        query = GetAdminQueryDTO.model_validate(obj=input_dto)
        response: GetAdminResponseDTO = await self._repository.get_admin(input_dto=query)
        return GetAdminOutputDTOV1.model_validate(obj=response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def get_admin_by_username(self, input_dto: GetAdminByUsernameInputDTOV1) -> GetAdminOutputDTOV1:
        query = GetAdminByUsernameQueryDTO.model_validate(obj=input_dto)
        response: GetAdminResponseDTO = await self._repository.get_admin_by_username(input_dto=query)
        return GetAdminOutputDTOV1.model_validate(obj=response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def search_admins(self, input_dto: SearchAdminInputDTOV1) -> SearchAdminOutputDTOV1:
        repository_dto = SearchAdminQueryDTO.model_validate(input_dto)
        response: SearchAdminResponseDTO = await self._repository.search_admins(input_dto=repository_dto)
        return SearchAdminOutputDTOV1.model_validate(response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def update_admin(self, input_dto: UpdateAdminInputDTOV1) -> None:
        command = UpdateAdminCommandDTO.model_validate(obj=input_dto)
        await self._repository.update_admin(input_dto=command)

    @async_postgres_sqlalchemy_atomic_decorator
    async def delete_admin(self, input_dto: DeleteAdminInputDTOV1) -> None:
        command = DeleteAdminCommandDTO.model_validate(obj=input_dto)
        await self._repository.delete_admin(input_dto=command)

