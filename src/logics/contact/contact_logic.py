from archipy.helpers.decorators.sqlalchemy_atomic import async_postgres_sqlalchemy_atomic_decorator
from archipy.helpers.utils.base_utils import BaseUtils

from src.repositories.contact.adapters.smtp_email_adapter import SmtpEmailAdapter
from src.configs.runtime_config import RuntimeConfig
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
        email_adapter: SmtpEmailAdapter,
    ) -> None:
        self._repository: ContactRepository = repository
        self._email_adapter: SmtpEmailAdapter = email_adapter

    async def create_contact_message(
        self,
        input_dto: CreateContactMessageInputDTOV1,
    ) -> CreateContactMessageOutputDTOV1:
        response = await self._create_contact_message_in_db(input_dto=input_dto)
        self._notify_new_contact_message(input_dto=input_dto)
        return response

    @async_postgres_sqlalchemy_atomic_decorator
    async def _create_contact_message_in_db(
        self,
        input_dto: CreateContactMessageInputDTOV1,
    ) -> CreateContactMessageOutputDTOV1:
        command = CreateContactMessageCommandDTO.model_validate(input_dto)
        response: CreateContactMessageResponseDTO = await self._repository.create_contact_message(input_dto=command)
        return CreateContactMessageOutputDTOV1.model_validate(obj=response)

    def _notify_new_contact_message(self, input_dto: CreateContactMessageInputDTOV1) -> None:
        notify_address = RuntimeConfig.global_config().CONTACT_NOTIFICATION_RECIPIENT_EMAIL
        if not notify_address:
            return

        try:
            self._email_adapter.send_email(
                to_email=notify_address,
                subject=f"New portfolio contact message from {input_dto.name}",
                body=f"From: {input_dto.name} <{input_dto.email}>\n\n{input_dto.message}",
            )
        except Exception as exception:
            BaseUtils.capture_exception(exception)

    @async_postgres_sqlalchemy_atomic_decorator
    async def search_contact_messages(
        self,
    ) -> SearchContactMessageOutputDTOV1:
        response: SearchContactMessageResponseDTO = await self._repository.search_contact_messages()
        return SearchContactMessageOutputDTOV1.model_validate(response)
