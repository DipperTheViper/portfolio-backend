from uuid import UUID

from archipy.models.dtos.base_dtos import BaseDTO
from pydantic import StrictStr


class CreateContactMessageInputDTOV1(BaseDTO):
    name: StrictStr
    email: StrictStr
    message: StrictStr
    is_read: bool = False


class CreateContactMessageOutputDTOV1(BaseDTO):
    contact_message_uuid: UUID


class ContactMessageItemDTOV1(BaseDTO):
    contact_message_uuid: UUID
    name: StrictStr
    email: StrictStr
    message: StrictStr
    is_read: bool


class SearchContactMessageOutputDTOV1(BaseDTO):
    contact_messages: list[ContactMessageItemDTOV1]
    total: int
