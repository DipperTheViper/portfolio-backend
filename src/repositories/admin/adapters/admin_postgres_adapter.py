from archipy.adapters.base.sqlalchemy.adapters import SQLAlchemyFilterMixin
from archipy.adapters.postgres.sqlalchemy.adapters import AsyncPostgresSQLAlchemyAdapter
from archipy.models.errors import NotFoundError
from archipy.models.types.base_types import FilterOperationType
from sqlalchemy import select
from sqlalchemy.sql.expression import Select

from src.models.dtos.admin.repository.admin_repository_interface_dtos import (
    GetAdminQueryDTO,
    GetAdminResponseDTO,
    SearchAdminResponseDTO,
    GetAdminByUsernameQueryDTO,
)
from src.models.entities import AdminEntity


class AdminPostgresAdapter(SQLAlchemyFilterMixin):
    def __init__(self, adapter: AsyncPostgresSQLAlchemyAdapter) -> None:
        self._adapter: AsyncPostgresSQLAlchemyAdapter = adapter

    async def get_admin(self, input_dto: GetAdminQueryDTO) -> GetAdminResponseDTO:
        select_query = select(AdminEntity).where(AdminEntity.is_deleted.is_(False))
        _query = self._apply_filter(
            query=select_query,
            field=AdminEntity.admin_uuid,
            value=input_dto.admin_uuid,
            operation=FilterOperationType.EQUAL,
        )
        result = await self._adapter.execute(statement=_query)
        entity = result.scalar()

        if not entity:
            raise NotFoundError(resource_type=AdminEntity.__name__)

        return GetAdminResponseDTO.model_validate(obj=entity)

    async def get_admin_by_username(self, input_dto: GetAdminByUsernameQueryDTO) -> GetAdminResponseDTO:
        select_query = select(AdminEntity).where(AdminEntity.is_deleted.is_(False))
        _query = self._apply_filter(
            query=select_query,
            field=AdminEntity.username,
            value=input_dto.username,
            operation=FilterOperationType.EQUAL,
        )
        result = await self._adapter.execute(statement=_query)
        entity = result.scalar()

        if not entity:
            raise NotFoundError(resource_type=AdminEntity.__name__)

        return GetAdminResponseDTO.model_validate(obj=entity)

    async def search_admins(self) -> SearchAdminResponseDTO:
        query: Select = select(AdminEntity).where(AdminEntity.is_deleted.is_(False))

        entities, total = await self._adapter.execute_search_query(
            query=query,
            entity=AdminEntity,
            sort_info=None,
            pagination=None,
        )

        return SearchAdminResponseDTO(admins=entities, total=total)
