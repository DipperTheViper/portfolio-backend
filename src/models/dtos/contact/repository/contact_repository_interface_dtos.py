from uuid import UUID

from archipy.models.dtos.base_dtos import BaseDTO
from pydantic import StrictStr


class CreateContactMessageCommandDTO(BaseDTO):
    name: StrictStr
    email: StrictStr
    message: StrictStr
    is_read: bool = False


class CreateContactMessageResponseDTO(BaseDTO):
    contact_message_uuid: UUID


class GetContactMessageResponseDTO(BaseDTO):
    contact_message_uuid: UUID
    name: StrictStr
    email: StrictStr
    message: StrictStr
    is_read: bool


class SearchContactMessageResponseDTO(BaseDTO):
    contact_messages: list[GetContactMessageResponseDTO]
    total: int
