from uuid import UUID

from archipy.models.dtos.base_dtos import BaseDTO
from pydantic import StrictStr


class GetAdminInputDTOV1(BaseDTO):
    admin_uuid: UUID


class GetAdminByUsernameInputDTOV1(BaseDTO):
    username: StrictStr


class GetAdminOutputDTOV1(BaseDTO):
    admin_uuid: UUID
    username: StrictStr
    is_active: bool


class GetAdminByUsernameOutputDTOV1(BaseDTO):
    admin_uuid: UUID
    username: StrictStr
    hashed_password: StrictStr
    is_active: bool


class AdminItemDTOV1(BaseDTO):
    admin_uuid: UUID
    username: StrictStr
    is_active: bool


class SearchAdminOutputDTOV1(BaseDTO):
    admins: list[AdminItemDTOV1]
    total: int
