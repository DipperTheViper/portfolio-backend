from archipy.adapters.base.sqlalchemy.adapters import SQLAlchemyFilterMixin
from archipy.adapters.postgres.sqlalchemy.adapters import AsyncPostgresSQLAlchemyAdapter
from sqlalchemy import select
from sqlalchemy.sql.expression import Select

from src.models.dtos.contact.repository.contact_repository_interface_dtos import (
    CreateContactMessageCommandDTO,
    CreateContactMessageResponseDTO,
    SearchContactMessageResponseDTO,
)
from src.models.entities import ContactMessageEntity


class ContactPostgresAdapter(SQLAlchemyFilterMixin):
    def __init__(self, adapter: AsyncPostgresSQLAlchemyAdapter) -> None:
        self._adapter: AsyncPostgresSQLAlchemyAdapter = adapter

    async def create_contact_message(
        self,
        input_dto: CreateContactMessageCommandDTO,
    ) -> CreateContactMessageResponseDTO:
        _entity = ContactMessageEntity(**input_dto.model_dump())
        result = await self._adapter.create(entity=_entity)
        return CreateContactMessageResponseDTO.model_validate(obj=result)

    async def search_contact_messages(self) -> SearchContactMessageResponseDTO:
        query: Select = select(ContactMessageEntity).where(ContactMessageEntity.is_deleted.is_(False))

        entities, total = await self._adapter.execute_search_query(
            query=query,
            entity=ContactMessageEntity,
            sort_info=None,
            pagination=None,
        )

        return SearchContactMessageResponseDTO(contact_messages=entities, total=total)
