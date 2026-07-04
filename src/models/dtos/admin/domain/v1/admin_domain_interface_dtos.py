from archipy.models.dtos.base_dtos import BaseDTO
from archipy.models.dtos.pagination_dto import PaginationDTO
from archipy.models.dtos.sort_dto import SortDTO
from archipy.models.types.sort_order_type import SortOrderType
from datetime import datetime, date, time
from decimal import Decimal
from pydantic import StrictStr
from uuid import UUID

from src.models.types.enums import *


class CreateAdminRestInputDTOV1(BaseDTO):
    username: StrictStr
    hashed_password: StrictStr
    is_active: bool


class CreateAdminInputDTOV1(CreateAdminRestInputDTOV1):
    @classmethod
    def create(
        cls,
        input_dto: CreateAdminRestInputDTOV1 = None,
    ):
        if input_dto:
            return cls(**input_dto.model_dump(mode="json"))
        return cls()


class CreateAdminOutputDTOV1(BaseDTO):
    admin_uuid: UUID


class GetAdminInputDTOV1(BaseDTO):
    admin_uuid: UUID


class GetAdminByUsernameInputDTOV1(BaseDTO):
    username: StrictStr


class GetAdminOutputDTOV1(BaseDTO):
    admin_uuid: UUID
    username: StrictStr
    hashed_password: StrictStr
    is_active: bool


class UpdateAdminRestInputDTOV1(BaseDTO):
    username: StrictStr | None = None
    hashed_password: StrictStr | None = None
    is_active: bool | None = None


class UpdateAdminInputDTOV1(UpdateAdminRestInputDTOV1):
    admin_uuid: UUID


class DeleteAdminInputDTOV1(BaseDTO):
    admin_uuid: UUID


class SearchAdminInputDTOV1(BaseDTO):
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


class AdminItemDTOV1(BaseDTO):
    admin_uuid: UUID
    username: StrictStr
    hashed_password: StrictStr
    is_active: bool


class SearchAdminOutputDTOV1(BaseDTO):
    admins: list[AdminItemDTOV1]
    total: int
