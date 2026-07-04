from uuid import UUID

from archipy.models.dtos.base_dtos import BaseDTO
from pydantic import StrictStr

from src.models.types.enums import FilePurposeType


class CreateFileInputDTOV1(BaseDTO):
    file_name: StrictStr
    content: bytes
    purpose_type: FilePurposeType


class CreateFileOutputDTOV1(BaseDTO):
    file_uuid: UUID


class GetFileInputDTOV1(BaseDTO):
    file_uuid: UUID


class UpdateFileInputDTOV1(BaseDTO):
    file_uuid: UUID
    file_name: StrictStr
    content: bytes


class DeleteFileInputDTOV1(BaseDTO):
    file_uuid: UUID


class FileItemDTOV1(BaseDTO):
    file_uuid: UUID
    file_name: StrictStr
    file_type: StrictStr
    purpose_type: StrictStr


class SearchFileOutputDTOV1(BaseDTO):
    files: list[FileItemDTOV1]
    total: int
