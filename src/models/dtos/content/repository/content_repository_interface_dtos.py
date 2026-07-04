from archipy.models.dtos.base_dtos import BaseDTO
from archipy.models.dtos.pagination_dto import PaginationDTO
from archipy.models.dtos.sort_dto import SortDTO
from datetime import datetime, date, time
from decimal import Decimal
from pydantic import StrictStr
from uuid import UUID

from src.models.types.enums import *


class CreateAboutCommandDTO(BaseDTO):
    lead: StrictStr
    body: StrictStr


class CreateAboutResponseDTO(BaseDTO):
    about_uuid: UUID


class GetAboutQueryDTO(BaseDTO):
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


class SearchAboutQueryDTO(BaseDTO):
    # TODO: Add search fields as needed
    pagination: PaginationDTO
    sort_info: SortDTO[str]


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


class GetExperienceQueryDTO(BaseDTO):
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


class SearchExperienceQueryDTO(BaseDTO):
    # TODO: Add search fields as needed
    pagination: PaginationDTO
    sort_info: SortDTO[str]


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


class GetHonorQueryDTO(BaseDTO):
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


class SearchHonorQueryDTO(BaseDTO):
    # TODO: Add search fields as needed
    pagination: PaginationDTO
    sort_info: SortDTO[str]


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


class GetProjectQueryDTO(BaseDTO):
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


class SearchProjectQueryDTO(BaseDTO):
    # TODO: Add search fields as needed
    pagination: PaginationDTO
    sort_info: SortDTO[str]


class SearchProjectResponseDTO(BaseDTO):
    projects: list[GetProjectResponseDTO]
    total: int


class CreateSkillCommandDTO(BaseDTO):
    group_name: StrictStr
    name: StrictStr
    display_order: int


class CreateSkillResponseDTO(BaseDTO):
    skill_uuid: UUID


class GetSkillQueryDTO(BaseDTO):
    skill_uuid: UUID


class GetSkillResponseDTO(BaseDTO):
    skill_uuid: UUID
    group_name: StrictStr
    name: StrictStr
    display_order: int


class UpdateSkillCommandDTO(BaseDTO):
    skill_uuid: UUID
    group_name: StrictStr | None = None
    name: StrictStr | None = None
    display_order: int | None = None


class DeleteSkillCommandDTO(BaseDTO):
    skill_uuid: UUID


class SearchSkillQueryDTO(BaseDTO):
    # TODO: Add search fields as needed
    pagination: PaginationDTO
    sort_info: SortDTO[str]


class SearchSkillResponseDTO(BaseDTO):
    skills: list[GetSkillResponseDTO]
    total: int

