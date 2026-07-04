from archipy.models.dtos.base_dtos import BaseDTO
from archipy.models.dtos.pagination_dto import PaginationDTO
from archipy.models.dtos.sort_dto import SortDTO
from archipy.models.types.sort_order_type import SortOrderType
from datetime import datetime, date, time
from decimal import Decimal
from pydantic import StrictStr
from uuid import UUID

from src.models.types.enums import *


class CreateAboutRestInputDTOV1(BaseDTO):
    lead: StrictStr
    body: StrictStr


class CreateAboutInputDTOV1(CreateAboutRestInputDTOV1):
    user_uuid: UUID | None = None

    @classmethod
    def create(
        cls,
        user_uuid: UUID | None = None,
        input_dto: CreateAboutRestInputDTOV1 = None,
    ):
        if input_dto:
            return cls(user_uuid=user_uuid, **input_dto.model_dump(mode="json"))
        return cls(user_uuid=user_uuid)


class CreateAboutOutputDTOV1(BaseDTO):
    about_uuid: UUID


class GetAboutInputDTOV1(BaseDTO):
    about_uuid: UUID


class GetAboutOutputDTOV1(BaseDTO):
    about_uuid: UUID
    lead: StrictStr
    body: StrictStr


class UpdateAboutRestInputDTOV1(BaseDTO):
    lead: StrictStr | None = None
    body: StrictStr | None = None


class UpdateAboutInputDTOV1(UpdateAboutRestInputDTOV1):
    about_uuid: UUID


class DeleteAboutInputDTOV1(BaseDTO):
    about_uuid: UUID


class SearchAboutInputDTOV1(BaseDTO):
    # TODO: Add search fields as needed
    pagination: PaginationDTO
    sort_info: SortDTO[str]  # Replace with appropriate sort enum

    @classmethod
    def create(
        cls,
        page: int = 1,
        page_size: int = 10,
        sort_column: str = "created_at",
        sort_order: SortOrderType = SortOrderType.DESCENDING,
    ):
        pagination = PaginationDTO(page=page, page_size=page_size)
        sort_info = SortDTO[str](column=sort_column, order=sort_order)
        return cls(pagination=pagination, sort_info=sort_info)


class AboutItemDTOV1(BaseDTO):
    about_uuid: UUID
    lead: StrictStr
    body: StrictStr


class SearchAboutOutputDTOV1(BaseDTO):
    abouts: list[AboutItemDTOV1]
    total: int


class CreateExperienceRestInputDTOV1(BaseDTO):
    display_order: int
    date_range: StrictStr
    role: StrictStr
    company: StrictStr
    description: StrictStr


class CreateExperienceInputDTOV1(CreateExperienceRestInputDTOV1):
    user_uuid: UUID | None = None

    @classmethod
    def create(
        cls,
        user_uuid: UUID | None = None,
        input_dto: CreateExperienceRestInputDTOV1 = None,
    ):
        if input_dto:
            return cls(user_uuid=user_uuid, **input_dto.model_dump(mode="json"))
        return cls(user_uuid=user_uuid)


class CreateExperienceOutputDTOV1(BaseDTO):
    experience_uuid: UUID


class GetExperienceInputDTOV1(BaseDTO):
    experience_uuid: UUID


class GetExperienceOutputDTOV1(BaseDTO):
    experience_uuid: UUID
    display_order: int
    date_range: StrictStr
    role: StrictStr
    company: StrictStr
    description: StrictStr


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


class SearchExperienceInputDTOV1(BaseDTO):
    # TODO: Add search fields as needed
    pagination: PaginationDTO
    sort_info: SortDTO[str]  # Replace with appropriate sort enum

    @classmethod
    def create(
        cls,
        page: int = 1,
        page_size: int = 10,
        sort_column: str = "created_at",
        sort_order: SortOrderType = SortOrderType.DESCENDING,
    ):
        pagination = PaginationDTO(page=page, page_size=page_size)
        sort_info = SortDTO[str](column=sort_column, order=sort_order)
        return cls(pagination=pagination, sort_info=sort_info)


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


class CreateHonorRestInputDTOV1(BaseDTO):
    display_order: int
    figure: StrictStr
    title: StrictStr
    detail: StrictStr


class CreateHonorInputDTOV1(CreateHonorRestInputDTOV1):
    user_uuid: UUID | None = None

    @classmethod
    def create(
        cls,
        user_uuid: UUID | None = None,
        input_dto: CreateHonorRestInputDTOV1 = None,
    ):
        if input_dto:
            return cls(user_uuid=user_uuid, **input_dto.model_dump(mode="json"))
        return cls(user_uuid=user_uuid)


class CreateHonorOutputDTOV1(BaseDTO):
    honor_uuid: UUID


class GetHonorInputDTOV1(BaseDTO):
    honor_uuid: UUID


class GetHonorOutputDTOV1(BaseDTO):
    honor_uuid: UUID
    display_order: int
    figure: StrictStr
    title: StrictStr
    detail: StrictStr


class UpdateHonorRestInputDTOV1(BaseDTO):
    display_order: int | None = None
    figure: StrictStr | None = None
    title: StrictStr | None = None
    detail: StrictStr | None = None


class UpdateHonorInputDTOV1(UpdateHonorRestInputDTOV1):
    honor_uuid: UUID


class DeleteHonorInputDTOV1(BaseDTO):
    honor_uuid: UUID


class SearchHonorInputDTOV1(BaseDTO):
    # TODO: Add search fields as needed
    pagination: PaginationDTO
    sort_info: SortDTO[str]  # Replace with appropriate sort enum

    @classmethod
    def create(
        cls,
        page: int = 1,
        page_size: int = 10,
        sort_column: str = "created_at",
        sort_order: SortOrderType = SortOrderType.DESCENDING,
    ):
        pagination = PaginationDTO(page=page, page_size=page_size)
        sort_info = SortDTO[str](column=sort_column, order=sort_order)
        return cls(pagination=pagination, sort_info=sort_info)


class HonorItemDTOV1(BaseDTO):
    honor_uuid: UUID
    display_order: int
    figure: StrictStr
    title: StrictStr
    detail: StrictStr


class SearchHonorOutputDTOV1(BaseDTO):
    honors: list[HonorItemDTOV1]
    total: int


class CreateProjectRestInputDTOV1(BaseDTO):
    display_order: int
    title: StrictStr
    date_range: StrictStr
    company: StrictStr
    role: StrictStr
    description: StrictStr
    tech_tags: StrictStr
    stats: StrictStr


class CreateProjectInputDTOV1(CreateProjectRestInputDTOV1):
    user_uuid: UUID | None = None

    @classmethod
    def create(
        cls,
        user_uuid: UUID | None = None,
        input_dto: CreateProjectRestInputDTOV1 = None,
    ):
        if input_dto:
            return cls(user_uuid=user_uuid, **input_dto.model_dump(mode="json"))
        return cls(user_uuid=user_uuid)


class CreateProjectOutputDTOV1(BaseDTO):
    project_uuid: UUID


class GetProjectInputDTOV1(BaseDTO):
    project_uuid: UUID


class GetProjectOutputDTOV1(BaseDTO):
    project_uuid: UUID
    display_order: int
    title: StrictStr
    date_range: StrictStr
    company: StrictStr
    role: StrictStr
    description: StrictStr
    tech_tags: StrictStr
    stats: StrictStr


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


class SearchProjectInputDTOV1(BaseDTO):
    # TODO: Add search fields as needed
    pagination: PaginationDTO
    sort_info: SortDTO[str]  # Replace with appropriate sort enum

    @classmethod
    def create(
        cls,
        page: int = 1,
        page_size: int = 10,
        sort_column: str = "created_at",
        sort_order: SortOrderType = SortOrderType.DESCENDING,
    ):
        pagination = PaginationDTO(page=page, page_size=page_size)
        sort_info = SortDTO[str](column=sort_column, order=sort_order)
        return cls(pagination=pagination, sort_info=sort_info)


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


class CreateSkillRestInputDTOV1(BaseDTO):
    group_name: StrictStr
    name: StrictStr
    display_order: int


class CreateSkillInputDTOV1(CreateSkillRestInputDTOV1):
    user_uuid: UUID | None = None

    @classmethod
    def create(
        cls,
        user_uuid: UUID | None = None,
        input_dto: CreateSkillRestInputDTOV1 = None,
    ):
        if input_dto:
            return cls(user_uuid=user_uuid, **input_dto.model_dump(mode="json"))
        return cls(user_uuid=user_uuid)


class CreateSkillOutputDTOV1(BaseDTO):
    skill_uuid: UUID


class GetSkillInputDTOV1(BaseDTO):
    skill_uuid: UUID


class GetSkillOutputDTOV1(BaseDTO):
    skill_uuid: UUID
    group_name: StrictStr
    name: StrictStr
    display_order: int


class UpdateSkillRestInputDTOV1(BaseDTO):
    group_name: StrictStr | None = None
    name: StrictStr | None = None
    display_order: int | None = None


class UpdateSkillInputDTOV1(UpdateSkillRestInputDTOV1):
    skill_uuid: UUID


class DeleteSkillInputDTOV1(BaseDTO):
    skill_uuid: UUID


class SearchSkillInputDTOV1(BaseDTO):
    # TODO: Add search fields as needed
    pagination: PaginationDTO
    sort_info: SortDTO[str]  # Replace with appropriate sort enum

    @classmethod
    def create(
        cls,
        page: int = 1,
        page_size: int = 10,
        sort_column: str = "created_at",
        sort_order: SortOrderType = SortOrderType.DESCENDING,
    ):
        pagination = PaginationDTO(page=page, page_size=page_size)
        sort_info = SortDTO[str](column=sort_column, order=sort_order)
        return cls(pagination=pagination, sort_info=sort_info)


class SkillItemDTOV1(BaseDTO):
    skill_uuid: UUID
    group_name: StrictStr
    name: StrictStr
    display_order: int


class SearchSkillOutputDTOV1(BaseDTO):
    skills: list[SkillItemDTOV1]
    total: int

