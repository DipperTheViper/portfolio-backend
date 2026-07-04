import uuid

from archipy.models.entities import UpdatableDeletableEntity
from sqlalchemy import Column, Boolean
from sqlalchemy.dialects.postgresql import UUID, VARCHAR
from sqlalchemy.orm import Mapped, Synonym, mapped_column, relationship


class AdminEntity(UpdatableDeletableEntity):
    __tablename__ = "admins"

    admin_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pk_uuid = Synonym("admin_uuid")

    username: Mapped[str] = mapped_column(VARCHAR(50), nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    # Relationships
    created_files = relationship("FileEntity", foreign_keys="[FileEntity.created_by]")
    updated_files = relationship("FileEntity", foreign_keys="[FileEntity.updated_by]")
