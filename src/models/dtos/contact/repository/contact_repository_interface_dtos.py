from archipy.models.dtos.base_dtos import BaseDTO
from archipy.models.dtos.pagination_dto import PaginationDTO
from archipy.models.dtos.sort_dto import SortDTO
from datetime import datetime, date, time
from decimal import Decimal
from pydantic import StrictStr
from uuid import UUID

from src.models.types.enums import *


class CreateContactMessageCommandDTO(BaseDTO):
    name: StrictStr
    email: StrictStr
    message: StrictStr
    is_read: bool


class CreateContactMessageResponseDTO(BaseDTO):
    contact_message_uuid: UUID


class GetContactMessageQueryDTO(BaseDTO):
    contact_message_uuid: UUID


class GetContactMessageResponseDTO(BaseDTO):
    contact_message_uuid: UUID
    name: StrictStr
    email: StrictStr
    message: StrictStr
    is_read: bool


class UpdateContactMessageCommandDTO(BaseDTO):
    contact_message_uuid: UUID
    name: StrictStr | None = None
    email: StrictStr | None = None
    message: StrictStr | None = None
    is_read: bool | None = None


class DeleteContactMessageCommandDTO(BaseDTO):
    contact_message_uuid: UUID


class SearchContactMessageQueryDTO(BaseDTO):
    # TODO: Add search fields as needed
    pagination: PaginationDTO
    sort_info: SortDTO[str]


class SearchContactMessageResponseDTO(BaseDTO):
    contact_messages: list[GetContactMessageResponseDTO]
    total: int

