from archipy.models.dtos.base_dtos import BaseDTO
from archipy.models.dtos.pagination_dto import PaginationDTO
from archipy.models.dtos.sort_dto import SortDTO
from datetime import datetime, date, time
from decimal import Decimal
from pydantic import StrictStr
from uuid import UUID

from src.models.types.enums import *


class CreateAdminCommandDTO(BaseDTO):
    username: StrictStr
    hashed_password: StrictStr
    is_active: bool


class CreateAdminResponseDTO(BaseDTO):
    admin_uuid: UUID


class GetAdminQueryDTO(BaseDTO):
    admin_uuid: UUID


class GetAdminByUsernameQueryDTO(BaseDTO):
    username: StrictStr


class GetAdminResponseDTO(BaseDTO):
    admin_uuid: UUID
    username: StrictStr
    hashed_password: StrictStr
    is_active: bool


class UpdateAdminCommandDTO(BaseDTO):
    admin_uuid: UUID
    username: StrictStr | None = None
    hashed_password: StrictStr | None = None
    is_active: bool | None = None


class DeleteAdminCommandDTO(BaseDTO):
    admin_uuid: UUID


class SearchAdminQueryDTO(BaseDTO):
    # TODO: Add search fields as needed
    pagination: PaginationDTO
    sort_info: SortDTO[str]


class SearchAdminResponseDTO(BaseDTO):
    admins: list[GetAdminResponseDTO]
    total: int
