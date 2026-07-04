from archipy.models.dtos.base_dtos import BaseDTO
from archipy.models.dtos.pagination_dto import PaginationDTO
from archipy.models.dtos.sort_dto import SortDTO
from archipy.models.types.sort_order_type import SortOrderType
from datetime import datetime, date, time
from decimal import Decimal
from pydantic import StrictStr
from uuid import UUID

from src.models.types.enums import *


class CreateContactMessageRestInputDTOV1(BaseDTO):
    name: StrictStr
    email: StrictStr
    message: StrictStr
    is_read: bool


class CreateContactMessageInputDTOV1(CreateContactMessageRestInputDTOV1):
    @classmethod
    def create(
        cls,
        input_dto: CreateContactMessageRestInputDTOV1 = None,
    ):
        if input_dto:
            return cls(**input_dto.model_dump(mode="json"))
        return cls()


class CreateContactMessageOutputDTOV1(BaseDTO):
    contact_message_uuid: UUID


class GetContactMessageInputDTOV1(BaseDTO):
    contact_message_uuid: UUID


class GetContactMessageOutputDTOV1(BaseDTO):
    contact_message_uuid: UUID
    name: StrictStr
    email: StrictStr
    message: StrictStr
    is_read: bool


class UpdateContactMessageRestInputDTOV1(BaseDTO):
    name: StrictStr | None = None
    email: StrictStr | None = None
    message: StrictStr | None = None
    is_read: bool | None = None


class UpdateContactMessageInputDTOV1(UpdateContactMessageRestInputDTOV1):
    contact_message_uuid: UUID


class DeleteContactMessageInputDTOV1(BaseDTO):
    contact_message_uuid: UUID


class SearchContactMessageInputDTOV1(BaseDTO):
    # TODO: Add search fields as needed
    pagination: PaginationDTO
    sort_info: SortDTO[str]  # Replace with appropriate sort enum

    @classmethod
    def create(
        cls,
        page: int = 1,
        page_size: int = 10,
        sort_column: str = "created_at",
        sort_order: SortOrderType = SortOrderType.DESCENDING,
    ):
        pagination = PaginationDTO(page=page, page_size=page_size)
        sort_info = SortDTO[str](column=sort_column, order=sort_order)
        return cls(pagination=pagination, sort_info=sort_info)


class ContactMessageItemDTOV1(BaseDTO):
    contact_message_uuid: UUID
    name: StrictStr
    email: StrictStr
    message: StrictStr
    is_read: bool


class SearchContactMessageOutputDTOV1(BaseDTO):
    contact_messages: list[ContactMessageItemDTOV1]
    total: int
