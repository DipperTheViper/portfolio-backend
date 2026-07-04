from archipy.helpers.decorators.sqlalchemy_atomic import async_postgres_sqlalchemy_atomic_decorator

from src.models.dtos.admin.domain.v1.admin_domain_interface_dtos import (
    GetAdminInputDTOV1,
    GetAdminOutputDTOV1,
    SearchAdminOutputDTOV1,
    GetAdminByUsernameInputDTOV1,
    GetAdminByUsernameOutputDTOV1,
)
from src.models.dtos.admin.repository.admin_repository_interface_dtos import (
    GetAdminQueryDTO,
    GetAdminResponseDTO,
    SearchAdminResponseDTO,
    GetAdminByUsernameQueryDTO,
)
from src.repositories.admin.admin_repository import AdminRepository


class AdminLogic:
    def __init__(
        self,
        repository: AdminRepository,
    ) -> None:
        self._repository: AdminRepository = repository

    @async_postgres_sqlalchemy_atomic_decorator
    async def get_admin(self, input_dto: GetAdminInputDTOV1) -> GetAdminOutputDTOV1:
        query = GetAdminQueryDTO.model_validate(obj=input_dto)
        response: GetAdminResponseDTO = await self._repository.get_admin(input_dto=query)
        return GetAdminOutputDTOV1.model_validate(obj=response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def get_admin_by_username(self, input_dto: GetAdminByUsernameInputDTOV1) -> GetAdminByUsernameOutputDTOV1:
        query = GetAdminByUsernameQueryDTO.model_validate(obj=input_dto)
        response: GetAdminResponseDTO = await self._repository.get_admin_by_username(input_dto=query)
        return GetAdminByUsernameOutputDTOV1.model_validate(obj=response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def search_admins(self) -> SearchAdminOutputDTOV1:
        response: SearchAdminResponseDTO = await self._repository.search_admins()
        return SearchAdminOutputDTOV1.model_validate(response)
