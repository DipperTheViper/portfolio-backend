import uuid

from archipy.models.entities import UpdatableDeletableEntity
from sqlalchemy import Boolean, Column
from sqlalchemy.dialects.postgresql import TEXT, UUID, VARCHAR
from sqlalchemy.orm import Mapped, Synonym, mapped_column


class ContactMessageEntity(UpdatableDeletableEntity):
    __tablename__ = "contact_messages"

    contact_message_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pk_uuid = Synonym("contact_message_uuid")

    name: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    email: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    message: Mapped[str] = mapped_column(TEXT, nullable=False)
    is_read: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
