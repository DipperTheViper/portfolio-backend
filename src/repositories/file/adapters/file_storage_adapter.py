import uuid
from pathlib import Path

from archipy.models.errors import InvalidArgumentError

from src.models.types.enums import FilePurposeType

_ALLOWED_EXTENSIONS_BY_PURPOSE: dict[FilePurposeType, frozenset[str]] = {
    FilePurposeType.RESUME: frozenset({"pdf"}),
}


class FileStorageAdapter:
    """Local on-disk storage for uploaded files.

    The on-disk filename is always a freshly generated uuid4, never the
    client-supplied filename or path - this is what prevents path traversal
    and overwrite attacks regardless of what a caller sends as the original
    filename.
    """

    def __init__(self, storage_dir: str, max_size_bytes: int) -> None:
        base_dir = Path(storage_dir)
        if not base_dir.is_absolute():
            base_dir = Path.cwd() / base_dir
        base_dir.mkdir(parents=True, exist_ok=True)

        self._base_dir: Path = base_dir
        self._max_size_bytes: int = max_size_bytes

    def save_file(self, content: bytes, file_name: str, purpose_type: FilePurposeType) -> str:
        extension = self._validate_extension(file_name=file_name, purpose_type=purpose_type)
        if not content or len(content) > self._max_size_bytes:
            raise InvalidArgumentError(argument_name="file")

        stored_name = f"{uuid.uuid4()}.{extension}"
        (self._base_dir / stored_name).write_bytes(content)
        return stored_name

    def delete_file(self, stored_name: str) -> None:
        (self._base_dir / stored_name).unlink(missing_ok=True)

    def get_file_path(self, stored_name: str) -> Path:
        return self._base_dir / stored_name

    @staticmethod
    def _validate_extension(file_name: str, purpose_type: FilePurposeType) -> str:
        extension = file_name.rsplit(".", 1)[-1].lower() if "." in file_name else ""
        allowed = _ALLOWED_EXTENSIONS_BY_PURPOSE.get(purpose_type, frozenset())
        if not extension or extension not in allowed:
            raise InvalidArgumentError(argument_name="file_name")
        return extension
