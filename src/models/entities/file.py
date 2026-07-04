import uuid
from typing import Optional

from archipy.models.entities import UpdatableDeletableEntity
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, VARCHAR
from sqlalchemy.orm import Mapped, Synonym, mapped_column, relationship


class FileEntity(UpdatableDeletableEntity):
    __tablename__ = "files"

    file_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pk_uuid = Synonym("file_uuid")

    file_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    path: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    file_type: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    purpose_type: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)

    # Foreign keys
    created_by: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("admins.admin_uuid"),
        nullable=True,
    )
    updated_by: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("admins.admin_uuid"),
        nullable=True,
    )

    # Relationships
    creator = relationship("AdminEntity", foreign_keys=[created_by])
    updater = relationship("AdminEntity", foreign_keys=[updated_by])
