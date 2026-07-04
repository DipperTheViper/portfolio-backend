from archipy.helpers.decorators.sqlalchemy_atomic import async_postgres_sqlalchemy_atomic_decorator

from src.models.dtos.contact.domain.v1.contact_domain_interface_dtos import (
    CreateContactMessageInputDTOV1,
    CreateContactMessageOutputDTOV1,
    SearchContactMessageOutputDTOV1,
)
from src.models.dtos.contact.repository.contact_repository_interface_dtos import (
    CreateContactMessageCommandDTO,
    CreateContactMessageResponseDTO,
    SearchContactMessageResponseDTO,
)
from src.repositories.contact.contact_repository import ContactRepository


class ContactLogic:
    def __init__(
        self,
        repository: ContactRepository,
    ) -> None:
        self._repository: ContactRepository = repository

    @async_postgres_sqlalchemy_atomic_decorator
    async def create_contact_message(
        self,
        input_dto: CreateContactMessageInputDTOV1,
    ) -> CreateContactMessageOutputDTOV1:
        command = CreateContactMessageCommandDTO.model_validate(input_dto)
        response: CreateContactMessageResponseDTO = await self._repository.create_contact_message(input_dto=command)
        return CreateContactMessageOutputDTOV1.model_validate(obj=response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def search_contact_messages(
        self,
    ) -> SearchContactMessageOutputDTOV1:
        response: SearchContactMessageResponseDTO = await self._repository.search_contact_messages()
        return SearchContactMessageOutputDTOV1.model_validate(response)
