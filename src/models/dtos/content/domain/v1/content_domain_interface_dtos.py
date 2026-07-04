from uuid import UUID

from archipy.models.dtos.base_dtos import BaseDTO
from pydantic import StrictStr

from src.models.types.enums import SkillGroupNameType


class CreateAboutInputDTOV1(BaseDTO):
    lead: StrictStr
    body: StrictStr


class CreateAboutOutputDTOV1(BaseDTO):
    about_uuid: UUID


class UpdateAboutRestInputDTOV1(BaseDTO):
    lead: StrictStr | None = None
    body: StrictStr | None = None


class UpdateAboutInputDTOV1(UpdateAboutRestInputDTOV1):
    about_uuid: UUID


class DeleteAboutInputDTOV1(BaseDTO):
    about_uuid: UUID


class AboutItemDTOV1(BaseDTO):
    about_uuid: UUID
    lead: StrictStr
    body: StrictStr


class SearchAboutOutputDTOV1(BaseDTO):
    abouts: list[AboutItemDTOV1]
    total: int


class CreateExperienceInputDTOV1(BaseDTO):
    display_order: int
    date_range: StrictStr
    role: StrictStr
    company: StrictStr
    description: StrictStr


class CreateExperienceOutputDTOV1(BaseDTO):
    experience_uuid: UUID


class UpdateExperienceRestInputDTOV1(BaseDTO):
    display_order: int | None = None
    date_range: StrictStr | None = None
    role: StrictStr | None = None
    company: StrictStr | None = None
    description: StrictStr | None = None


class UpdateExperienceInputDTOV1(UpdateExperienceRestInputDTOV1):
    experience_uuid: UUID


class DeleteExperienceInputDTOV1(BaseDTO):
    experience_uuid: UUID


class ExperienceItemDTOV1(BaseDTO):
    experience_uuid: UUID
    display_order: int
    date_range: StrictStr
    role: StrictStr
    company: StrictStr
    description: StrictStr


class SearchExperienceOutputDTOV1(BaseDTO):
    experiences: list[ExperienceItemDTOV1]
    total: int


class CreateHonorInputDTOV1(BaseDTO):
    display_order: int
    figure: StrictStr
    title: StrictStr
    detail: StrictStr


class CreateHonorOutputDTOV1(BaseDTO):
    honor_uuid: UUID


class UpdateHonorRestInputDTOV1(BaseDTO):
    display_order: int | None = None
    figure: StrictStr | None = None
    title: StrictStr | None = None
    detail: StrictStr | None = None


class UpdateHonorInputDTOV1(UpdateHonorRestInputDTOV1):
    honor_uuid: UUID


class DeleteHonorInputDTOV1(BaseDTO):
    honor_uuid: UUID


class HonorItemDTOV1(BaseDTO):
    honor_uuid: UUID
    display_order: int
    figure: StrictStr
    title: StrictStr
    detail: StrictStr


class SearchHonorOutputDTOV1(BaseDTO):
    honors: list[HonorItemDTOV1]
    total: int


class CreateProjectInputDTOV1(BaseDTO):
    display_order: int
    title: StrictStr
    date_range: StrictStr
    company: StrictStr
    role: StrictStr
    description: StrictStr
    tech_tags: StrictStr
    stats: StrictStr


class CreateProjectOutputDTOV1(BaseDTO):
    project_uuid: UUID


class UpdateProjectRestInputDTOV1(BaseDTO):
    display_order: int | None = None
    title: StrictStr | None = None
    date_range: StrictStr | None = None
    company: StrictStr | None = None
    role: StrictStr | None = None
    description: StrictStr | None = None
    tech_tags: StrictStr | None = None
    stats: StrictStr | None = None


class UpdateProjectInputDTOV1(UpdateProjectRestInputDTOV1):
    project_uuid: UUID


class DeleteProjectInputDTOV1(BaseDTO):
    project_uuid: UUID


class ProjectItemDTOV1(BaseDTO):
    project_uuid: UUID
    display_order: int
    title: StrictStr
    date_range: StrictStr
    company: StrictStr
    role: StrictStr
    description: StrictStr
    tech_tags: StrictStr
    stats: StrictStr


class SearchProjectOutputDTOV1(BaseDTO):
    projects: list[ProjectItemDTOV1]
    total: int


class CreateSkillInputDTOV1(BaseDTO):
    group_name: SkillGroupNameType
    name: StrictStr
    display_order: int


class CreateSkillOutputDTOV1(BaseDTO):
    skill_uuid: UUID


class UpdateSkillRestInputDTOV1(BaseDTO):
    group_name: SkillGroupNameType | None = None
    name: StrictStr | None = None
    display_order: int | None = None


class UpdateSkillInputDTOV1(UpdateSkillRestInputDTOV1):
    skill_uuid: UUID


class DeleteSkillInputDTOV1(BaseDTO):
    skill_uuid: UUID


class SkillItemDTOV1(BaseDTO):
    skill_uuid: UUID
    group_name: SkillGroupNameType
    name: StrictStr
    display_order: int


class SearchSkillOutputDTOV1(BaseDTO):
    skills: list[SkillItemDTOV1]
    total: int
