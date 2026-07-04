from archipy.models.dtos.base_dtos import BaseDTO
from archipy.models.dtos.pagination_dto import PaginationDTO
from archipy.models.dtos.sort_dto import SortDTO
from datetime import datetime, date, time
from decimal import Decimal
from pydantic import StrictStr
from uuid import UUID

from src.models.types.enums import *


class CreateFileCommandDTO(BaseDTO):
    file_name: StrictStr
    path: StrictStr
    file_type: StrictStr
    purpose_type: StrictStr
    created_by: UUID | None = None
    updated_by: UUID | None = None


class CreateFileResponseDTO(BaseDTO):
    file_uuid: UUID


class GetFileQueryDTO(BaseDTO):
    file_uuid: UUID


class GetFileResponseDTO(BaseDTO):
    file_uuid: UUID
    file_name: StrictStr
    path: StrictStr
    file_type: StrictStr
    purpose_type: StrictStr
    created_by: UUID | None = None
    updated_by: UUID | None = None


class UpdateFileCommandDTO(BaseDTO):
    file_uuid: UUID
    file_name: StrictStr | None = None
    path: StrictStr | None = None
    file_type: StrictStr | None = None
    purpose_type: StrictStr | None = None
    created_by: UUID | None = None
    updated_by: UUID | None = None


class DeleteFileCommandDTO(BaseDTO):
    file_uuid: UUID


class SearchFileQueryDTO(BaseDTO):
    # TODO: Add search fields as needed
    pagination: PaginationDTO
    sort_info: SortDTO[str]


class SearchFileResponseDTO(BaseDTO):
    files: list[GetFileResponseDTO]
    total: int
