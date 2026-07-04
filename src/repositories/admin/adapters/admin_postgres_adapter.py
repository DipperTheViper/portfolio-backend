from archipy.adapters.base.sqlalchemy.adapters import SQLAlchemyFilterMixin
from archipy.adapters.postgres.sqlalchemy.adapters import AsyncPostgresSQLAlchemyAdapter
from archipy.models.errors import NotFoundError
from archipy.models.types.base_types import FilterOperationType
from sqlalchemy import delete, select, update, func, or_
from sqlalchemy.orm import selectinload
from sqlalchemy.sql.expression import Select, Update

from src.models.dtos.admin.repository.admin_repository_interface_dtos import (
    CreateAdminCommandDTO,
    CreateAdminResponseDTO,
    GetAdminQueryDTO,
    GetAdminByUsernameQueryDTO,
    GetAdminResponseDTO,
    UpdateAdminCommandDTO,
    DeleteAdminCommandDTO,
    SearchAdminQueryDTO,
    SearchAdminResponseDTO,
)
from src.models.entities import AdminEntity


class AdminPostgresAdapter(SQLAlchemyFilterMixin):
    def __init__(self, adapter: AsyncPostgresSQLAlchemyAdapter) -> None:
        self._adapter: AsyncPostgresSQLAlchemyAdapter = adapter

    async def create_admin(self, input_dto: CreateAdminCommandDTO) -> CreateAdminResponseDTO:
        _entity = AdminEntity(**input_dto.model_dump())
        result = await self._adapter.create(entity=_entity)
        return CreateAdminResponseDTO.model_validate(obj=result)

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

    async def search_admins(self, input_dto: SearchAdminQueryDTO) -> SearchAdminResponseDTO:
        query: Select = select(AdminEntity).where(AdminEntity.is_deleted.is_(False))

        if input_dto.user_uuid:
            query = self._apply_filter(
                query=query,
                field=AdminEntity.user_uuid,
                value=input_dto.user_uuid,
                operation=FilterOperationType.EQUAL,
            )

        entities, total = await self._adapter.execute_search_query(
            query=query,
            entity=AdminEntity,
            sort_info=input_dto.sort_info,
            pagination=input_dto.pagination,
        )

        return SearchAdminResponseDTO(admins=entities, total=total)

    async def update_admin(self, input_dto: UpdateAdminCommandDTO) -> None:
        update_data = input_dto.model_dump(exclude={"admin_uuid"}, exclude_none=True)
        if not update_data:
            return

        update_query: Update = (
            update(AdminEntity)
            .where(
                AdminEntity.admin_uuid == input_dto.admin_uuid,
                AdminEntity.is_deleted.is_(False),
            )
            .values(**update_data)
        )

        result = await self._adapter.execute(statement=update_query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=AdminEntity.__name__)

    async def delete_admin(self, input_dto: DeleteAdminCommandDTO) -> None:
        delete_query = (
            update(AdminEntity)
            .where(
                AdminEntity.admin_uuid == input_dto.admin_uuid,
                AdminEntity.is_deleted.is_(False),
            )
            .values(is_deleted=True)
        )

        result = await self._adapter.execute(statement=delete_query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=AdminEntity.__name__)
