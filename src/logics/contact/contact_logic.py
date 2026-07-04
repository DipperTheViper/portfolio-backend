from archipy.helpers.decorators.sqlalchemy_atomic import async_postgres_sqlalchemy_atomic_decorator
from uuid import UUID

from src.models.dtos.contact.domain.v1.contact_domain_interface_dtos import (
    CreateContactMessageInputDTOV1, CreateContactMessageOutputDTOV1, GetContactMessageInputDTOV1, GetContactMessageOutputDTOV1, UpdateContactMessageInputDTOV1, DeleteContactMessageInputDTOV1, SearchContactMessageInputDTOV1, SearchContactMessageOutputDTOV1
)
from src.models.dtos.contact.repository.contact_repository_interface_dtos import (
    CreateContactMessageCommandDTO, CreateContactMessageResponseDTO, GetContactMessageQueryDTO, GetContactMessageResponseDTO, UpdateContactMessageCommandDTO, DeleteContactMessageCommandDTO, SearchContactMessageQueryDTO, SearchContactMessageResponseDTO
)
from src.repositories.contact.contact_repository import ContactRepository


class ContactLogic:
    def __init__(
        self,
        repository: ContactRepository,
    ) -> None:
        self._repository: ContactRepository = repository

    @async_postgres_sqlalchemy_atomic_decorator
    async def create_contact_message(self, input_dto: CreateContactMessageInputDTOV1) -> CreateContactMessageOutputDTOV1:
        command = CreateContactMessageCommandDTO.model_validate(input_dto)
        response: CreateContactMessageResponseDTO = await self._repository.create_contact_message(input_dto=command)
        return CreateContactMessageOutputDTOV1.model_validate(obj=response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def get_contact_message(self, input_dto: GetContactMessageInputDTOV1) -> GetContactMessageOutputDTOV1:
        query = GetContactMessageQueryDTO.model_validate(obj=input_dto)
        response: GetContactMessageResponseDTO = await self._repository.get_contact_message(input_dto=query)
        return GetContactMessageOutputDTOV1.model_validate(obj=response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def search_contact_messages(self, input_dto: SearchContactMessageInputDTOV1) -> SearchContactMessageOutputDTOV1:
        repository_dto = SearchContactMessageQueryDTO.model_validate(input_dto)
        response: SearchContactMessageResponseDTO = await self._repository.search_contact_messages(input_dto=repository_dto)
        return SearchContactMessageOutputDTOV1.model_validate(response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def update_contact_message(self, input_dto: UpdateContactMessageInputDTOV1) -> None:
        command = UpdateContactMessageCommandDTO.model_validate(obj=input_dto)
        await self._repository.update_contact_message(input_dto=command)

    @async_postgres_sqlalchemy_atomic_decorator
    async def delete_contact_message(self, input_dto: DeleteContactMessageInputDTOV1) -> None:
        command = DeleteContactMessageCommandDTO.model_validate(obj=input_dto)
        await self._repository.delete_contact_message(input_dto=command)

