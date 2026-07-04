from uuid import UUID

from archipy.models.dtos.base_dtos import BaseDTO
from pydantic import StrictStr


class GetAdminQueryDTO(BaseDTO):
    admin_uuid: UUID


class GetAdminByUsernameQueryDTO(BaseDTO):
    username: StrictStr


class GetAdminResponseDTO(BaseDTO):
    admin_uuid: UUID
    username: StrictStr
    hashed_password: StrictStr
    is_active: bool


class SearchAdminResponseDTO(BaseDTO):
    admins: list[GetAdminResponseDTO]
    total: int
