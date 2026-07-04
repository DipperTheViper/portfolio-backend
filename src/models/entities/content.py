import uuid

from archipy.models.entities import UpdatableDeletableEntity
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import ARRAY, JSONB, TEXT, UUID, VARCHAR
from sqlalchemy.orm import Mapped, Synonym, mapped_column


class ProjectEntity(UpdatableDeletableEntity):
    __tablename__ = "projects"

    project_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pk_uuid = Synonym("project_uuid")

    display_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    title: Mapped[str] = mapped_column(VARCHAR(150), nullable=False)
    date_range: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    company: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    role: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    description: Mapped[str] = mapped_column(TEXT, nullable=False)
    tech_tags: Mapped[list[str]] = mapped_column(ARRAY(VARCHAR(50)), nullable=False, default=list)
    stats: Mapped[list[dict]] = mapped_column(JSONB, nullable=False, default=list)


class SkillEntity(UpdatableDeletableEntity):
    __tablename__ = "skills"

    skill_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pk_uuid = Synonym("skill_uuid")

    group_name: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    name: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)


class ExperienceEntity(UpdatableDeletableEntity):
    __tablename__ = "experiences"

    experience_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pk_uuid = Synonym("experience_uuid")

    display_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    date_range: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    role: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    company: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    description: Mapped[str] = mapped_column(TEXT, nullable=False)


class HonorEntity(UpdatableDeletableEntity):
    __tablename__ = "honors"

    honor_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pk_uuid = Synonym("honor_uuid")

    display_order: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    figure: Mapped[str] = mapped_column(VARCHAR(20), nullable=False)
    title: Mapped[str] = mapped_column(VARCHAR(150), nullable=False)
    detail: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)


class AboutEntity(UpdatableDeletableEntity):
    __tablename__ = "about"

    about_uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pk_uuid = Synonym("about_uuid")

    lead: Mapped[str] = mapped_column(TEXT, nullable=False)
    body: Mapped[str] = mapped_column(TEXT, nullable=False)
