from uuid import UUID

from archipy.models.dtos.base_dtos import BaseDTO
from pydantic import StrictStr

from src.models.types.enums import *


class CreateAboutCommandDTO(BaseDTO):
    lead: StrictStr
    body: StrictStr


class CreateAboutResponseDTO(BaseDTO):
    about_uuid: UUID


class GetAboutResponseDTO(BaseDTO):
    about_uuid: UUID
    lead: StrictStr
    body: StrictStr


class UpdateAboutCommandDTO(BaseDTO):
    about_uuid: UUID
    lead: StrictStr | None = None
    body: StrictStr | None = None


class DeleteAboutCommandDTO(BaseDTO):
    about_uuid: UUID


class SearchAboutResponseDTO(BaseDTO):
    abouts: list[GetAboutResponseDTO]
    total: int


class CreateExperienceCommandDTO(BaseDTO):
    display_order: int
    date_range: StrictStr
    role: StrictStr
    company: StrictStr
    description: StrictStr


class CreateExperienceResponseDTO(BaseDTO):
    experience_uuid: UUID


class GetExperienceResponseDTO(BaseDTO):
    experience_uuid: UUID
    display_order: int
    date_range: StrictStr
    role: StrictStr
    company: StrictStr
    description: StrictStr


class UpdateExperienceCommandDTO(BaseDTO):
    experience_uuid: UUID
    display_order: int | None = None
    date_range: StrictStr | None = None
    role: StrictStr | None = None
    company: StrictStr | None = None
    description: StrictStr | None = None


class DeleteExperienceCommandDTO(BaseDTO):
    experience_uuid: UUID


class SearchExperienceResponseDTO(BaseDTO):
    experiences: list[GetExperienceResponseDTO]
    total: int


class CreateHonorCommandDTO(BaseDTO):
    display_order: int
    figure: StrictStr
    title: StrictStr
    detail: StrictStr


class CreateHonorResponseDTO(BaseDTO):
    honor_uuid: UUID


class GetHonorResponseDTO(BaseDTO):
    honor_uuid: UUID
    display_order: int
    figure: StrictStr
    title: StrictStr
    detail: StrictStr


class UpdateHonorCommandDTO(BaseDTO):
    honor_uuid: UUID
    display_order: int | None = None
    figure: StrictStr | None = None
    title: StrictStr | None = None
    detail: StrictStr | None = None


class DeleteHonorCommandDTO(BaseDTO):
    honor_uuid: UUID


class SearchHonorResponseDTO(BaseDTO):
    honors: list[GetHonorResponseDTO]
    total: int


class CreateProjectCommandDTO(BaseDTO):
    display_order: int
    title: StrictStr
    date_range: StrictStr
    company: StrictStr
    role: StrictStr
    description: StrictStr
    tech_tags: StrictStr
    stats: StrictStr


class CreateProjectResponseDTO(BaseDTO):
    project_uuid: UUID


class GetProjectResponseDTO(BaseDTO):
    project_uuid: UUID
    display_order: int
    title: StrictStr
    date_range: StrictStr
    company: StrictStr
    role: StrictStr
    description: StrictStr
    tech_tags: StrictStr
    stats: StrictStr


class UpdateProjectCommandDTO(BaseDTO):
    project_uuid: UUID
    display_order: int | None = None
    title: StrictStr | None = None
    date_range: StrictStr | None = None
    company: StrictStr | None = None
    role: StrictStr | None = None
    description: StrictStr | None = None
    tech_tags: StrictStr | None = None
    stats: StrictStr | None = None


class DeleteProjectCommandDTO(BaseDTO):
    project_uuid: UUID


class SearchProjectResponseDTO(BaseDTO):
    projects: list[GetProjectResponseDTO]
    total: int


class CreateSkillCommandDTO(BaseDTO):
    group_name: SkillGroupNameType
    name: StrictStr
    display_order: int


class CreateSkillResponseDTO(BaseDTO):
    skill_uuid: UUID


class GetSkillResponseDTO(BaseDTO):
    skill_uuid: UUID
    group_name: SkillGroupNameType
    name: StrictStr
    display_order: int


class UpdateSkillCommandDTO(BaseDTO):
    skill_uuid: UUID
    group_name: SkillGroupNameType | None = None
    name: StrictStr | None = None
    display_order: int | None = None


class DeleteSkillCommandDTO(BaseDTO):
    skill_uuid: UUID


class SearchSkillResponseDTO(BaseDTO):
    skills: list[GetSkillResponseDTO]
    total: int
