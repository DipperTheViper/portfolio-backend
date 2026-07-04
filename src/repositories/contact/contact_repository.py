from src.models.dtos.contact.repository.contact_repository_interface_dtos import (
    CreateContactMessageCommandDTO, CreateContactMessageResponseDTO, GetContactMessageQueryDTO, GetContactMessageResponseDTO, UpdateContactMessageCommandDTO, DeleteContactMessageCommandDTO, SearchContactMessageQueryDTO, SearchContactMessageResponseDTO
)
from src.repositories.contact.adapters.contact_postgres_adapter import ContactPostgresAdapter


class ContactRepository:
    def __init__(self, postgres_adapter: ContactPostgresAdapter):
        self._postgres_adapter: ContactPostgresAdapter = postgres_adapter

    async def create_contact_message(self, input_dto: CreateContactMessageCommandDTO) -> CreateContactMessageResponseDTO:
        return await self._postgres_adapter.create_contact_message(input_dto=input_dto)

    async def get_contact_message(self, input_dto: GetContactMessageQueryDTO) -> GetContactMessageResponseDTO:
        return await self._postgres_adapter.get_contact_message(input_dto=input_dto)

    async def search_contact_messages(self, input_dto: SearchContactMessageQueryDTO) -> SearchContactMessageResponseDTO:
        return await self._postgres_adapter.search_contact_messages(input_dto=input_dto)

    async def update_contact_message(self, input_dto: UpdateContactMessageCommandDTO) -> None:
        await self._postgres_adapter.update_contact_message(input_dto=input_dto)

    async def delete_contact_message(self, input_dto: DeleteContactMessageCommandDTO) -> None:
        await self._postgres_adapter.delete_contact_message(input_dto=input_dto)

