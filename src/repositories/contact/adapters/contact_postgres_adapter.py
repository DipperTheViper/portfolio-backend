from archipy.adapters.base.sqlalchemy.adapters import SQLAlchemyFilterMixin
from archipy.adapters.postgres.sqlalchemy.adapters import AsyncPostgresSQLAlchemyAdapter
from archipy.models.errors import NotFoundError
from archipy.models.types.base_types import FilterOperationType
from sqlalchemy import delete, select, update, func, or_
from sqlalchemy.orm import selectinload
from sqlalchemy.sql.expression import Select, Update

from src.models.dtos.contact.repository.contact_repository_interface_dtos import (
    CreateContactMessageCommandDTO, CreateContactMessageResponseDTO, GetContactMessageQueryDTO, GetContactMessageResponseDTO, UpdateContactMessageCommandDTO, DeleteContactMessageCommandDTO, SearchContactMessageQueryDTO, SearchContactMessageResponseDTO
)
from src.models.entities import ContactMessageEntity


class ContactPostgresAdapter(SQLAlchemyFilterMixin):
    def __init__(self, adapter: AsyncPostgresSQLAlchemyAdapter) -> None:
        self._adapter: AsyncPostgresSQLAlchemyAdapter = adapter

    async def create_contact_message(self, input_dto: CreateContactMessageCommandDTO) -> CreateContactMessageResponseDTO:
        _entity = ContactMessageEntity(**input_dto.model_dump())
        result = await self._adapter.create(entity=_entity)
        return CreateContactMessageResponseDTO.model_validate(obj=result)

    async def get_contact_message(self, input_dto: GetContactMessageQueryDTO) -> GetContactMessageResponseDTO:
        select_query = select(ContactMessageEntity).where(ContactMessageEntity.is_deleted.is_(False))
        _query = self._apply_filter(
            query=select_query,
            field=ContactMessageEntity.contact_message_uuid,
            value=input_dto.contact_message_uuid,
            operation=FilterOperationType.EQUAL,
        )
        result = await self._adapter.execute(statement=_query)
        entity = result.scalar()

        if not entity:
            raise NotFoundError(resource_type=ContactMessageEntity.__name__)

        return GetContactMessageResponseDTO.model_validate(obj=entity)

    async def search_contact_messages(self, input_dto: SearchContactMessageQueryDTO) -> SearchContactMessageResponseDTO:
        query: Select = select(ContactMessageEntity).where(ContactMessageEntity.is_deleted.is_(False))

        if input_dto.user_uuid:
            query = self._apply_filter(
                query=query,
                field=ContactMessageEntity.user_uuid,
                value=input_dto.user_uuid,
                operation=FilterOperationType.EQUAL,
            )

        entities, total = await self._adapter.execute_search_query(
            query=query,
            entity=ContactMessageEntity,
            sort_info=input_dto.sort_info,
            pagination=input_dto.pagination,
        )

        return SearchContactMessageResponseDTO(contact_messages=entities, total=total)

    async def update_contact_message(self, input_dto: UpdateContactMessageCommandDTO) -> None:
        update_data = input_dto.model_dump(exclude={"contact_message_uuid"}, exclude_none=True)
        if not update_data:
            return

        update_query: Update = (
            update(ContactMessageEntity)
            .where(
                ContactMessageEntity.contact_message_uuid == input_dto.contact_message_uuid,
                ContactMessageEntity.is_deleted.is_(False),
            )
            .values(**update_data)
        )

        result = await self._adapter.execute(statement=update_query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=ContactMessageEntity.__name__)

    async def delete_contact_message(self, input_dto: DeleteContactMessageCommandDTO) -> None:
        delete_query = (
            update(ContactMessageEntity)
            .where(
                ContactMessageEntity.contact_message_uuid == input_dto.contact_message_uuid,
                ContactMessageEntity.is_deleted.is_(False),
            )
            .values(is_deleted=True)
        )

        result = await self._adapter.execute(statement=delete_query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=ContactMessageEntity.__name__)

