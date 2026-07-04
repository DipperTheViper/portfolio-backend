from archipy.adapters.base.sqlalchemy.adapters import SQLAlchemyFilterMixin
from archipy.adapters.postgres.sqlalchemy.adapters import AsyncPostgresSQLAlchemyAdapter
from archipy.models.errors import NotFoundError
from archipy.models.types.base_types import FilterOperationType
from sqlalchemy import delete, select, update, func, or_
from sqlalchemy.orm import selectinload
from sqlalchemy.sql.expression import Select, Update

from src.models.dtos.content.repository.content_repository_interface_dtos import (
    CreateAboutCommandDTO,
    CreateAboutResponseDTO,
    GetAboutQueryDTO,
    GetAboutResponseDTO,
    UpdateAboutCommandDTO,
    DeleteAboutCommandDTO,
    SearchAboutQueryDTO,
    SearchAboutResponseDTO,
    CreateExperienceCommandDTO,
    CreateExperienceResponseDTO,
    GetExperienceQueryDTO,
    GetExperienceResponseDTO,
    UpdateExperienceCommandDTO,
    DeleteExperienceCommandDTO,
    SearchExperienceQueryDTO,
    SearchExperienceResponseDTO,
    CreateHonorCommandDTO,
    CreateHonorResponseDTO,
    GetHonorQueryDTO,
    GetHonorResponseDTO,
    UpdateHonorCommandDTO,
    DeleteHonorCommandDTO,
    SearchHonorQueryDTO,
    SearchHonorResponseDTO,
    CreateProjectCommandDTO,
    CreateProjectResponseDTO,
    GetProjectQueryDTO,
    GetProjectResponseDTO,
    UpdateProjectCommandDTO,
    DeleteProjectCommandDTO,
    SearchProjectQueryDTO,
    SearchProjectResponseDTO,
    CreateSkillCommandDTO,
    CreateSkillResponseDTO,
    GetSkillQueryDTO,
    GetSkillResponseDTO,
    UpdateSkillCommandDTO,
    DeleteSkillCommandDTO,
    SearchSkillQueryDTO,
    SearchSkillResponseDTO,
)
from src.models.entities import AboutEntity, ExperienceEntity, HonorEntity, ProjectEntity, SkillEntity


class ContentPostgresAdapter(SQLAlchemyFilterMixin):
    def __init__(self, adapter: AsyncPostgresSQLAlchemyAdapter) -> None:
        self._adapter: AsyncPostgresSQLAlchemyAdapter = adapter

    async def create_about(self, input_dto: CreateAboutCommandDTO) -> CreateAboutResponseDTO:
        _entity = AboutEntity(**input_dto.model_dump())
        result = await self._adapter.create(entity=_entity)
        return CreateAboutResponseDTO.model_validate(obj=result)

    async def get_about(self, input_dto: GetAboutQueryDTO) -> GetAboutResponseDTO:
        select_query = select(AboutEntity).where(AboutEntity.is_deleted.is_(False))
        _query = self._apply_filter(
            query=select_query,
            field=AboutEntity.about_uuid,
            value=input_dto.about_uuid,
            operation=FilterOperationType.EQUAL,
        )
        result = await self._adapter.execute(statement=_query)
        entity = result.scalar()

        if not entity:
            raise NotFoundError(resource_type=AboutEntity.__name__)

        return GetAboutResponseDTO.model_validate(obj=entity)

    async def search_abouts(self, input_dto: SearchAboutQueryDTO) -> SearchAboutResponseDTO:
        query: Select = select(AboutEntity).where(AboutEntity.is_deleted.is_(False))

        entities, total = await self._adapter.execute_search_query(
            query=query,
            entity=AboutEntity,
            sort_info=input_dto.sort_info,
            pagination=input_dto.pagination,
        )

        return SearchAboutResponseDTO(abouts=entities, total=total)

    async def update_about(self, input_dto: UpdateAboutCommandDTO) -> None:
        update_data = input_dto.model_dump(exclude={"about_uuid"}, exclude_none=True)
        if not update_data:
            return

        update_query: Update = (
            update(AboutEntity)
            .where(
                AboutEntity.about_uuid == input_dto.about_uuid,
                AboutEntity.is_deleted.is_(False),
            )
            .values(**update_data)
        )

        result = await self._adapter.execute(statement=update_query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=AboutEntity.__name__)

    async def delete_about(self, input_dto: DeleteAboutCommandDTO) -> None:
        delete_query = (
            update(AboutEntity)
            .where(
                AboutEntity.about_uuid == input_dto.about_uuid,
                AboutEntity.is_deleted.is_(False),
            )
            .values(is_deleted=True)
        )

        result = await self._adapter.execute(statement=delete_query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=AboutEntity.__name__)

    async def create_experience(self, input_dto: CreateExperienceCommandDTO) -> CreateExperienceResponseDTO:
        _entity = ExperienceEntity(**input_dto.model_dump())
        result = await self._adapter.create(entity=_entity)
        return CreateExperienceResponseDTO.model_validate(obj=result)

    async def get_experience(self, input_dto: GetExperienceQueryDTO) -> GetExperienceResponseDTO:
        select_query = select(ExperienceEntity).where(ExperienceEntity.is_deleted.is_(False))
        _query = self._apply_filter(
            query=select_query,
            field=ExperienceEntity.experience_uuid,
            value=input_dto.experience_uuid,
            operation=FilterOperationType.EQUAL,
        )
        result = await self._adapter.execute(statement=_query)
        entity = result.scalar()

        if not entity:
            raise NotFoundError(resource_type=ExperienceEntity.__name__)

        return GetExperienceResponseDTO.model_validate(obj=entity)

    async def search_experiences(self, input_dto: SearchExperienceQueryDTO) -> SearchExperienceResponseDTO:
        query: Select = select(ExperienceEntity).where(ExperienceEntity.is_deleted.is_(False))

        entities, total = await self._adapter.execute_search_query(
            query=query,
            entity=ExperienceEntity,
            sort_info=input_dto.sort_info,
            pagination=input_dto.pagination,
        )

        return SearchExperienceResponseDTO(experiences=entities, total=total)

    async def update_experience(self, input_dto: UpdateExperienceCommandDTO) -> None:
        update_data = input_dto.model_dump(exclude={"experience_uuid"}, exclude_none=True)
        if not update_data:
            return

        update_query: Update = (
            update(ExperienceEntity)
            .where(
                ExperienceEntity.experience_uuid == input_dto.experience_uuid,
                ExperienceEntity.is_deleted.is_(False),
            )
            .values(**update_data)
        )

        result = await self._adapter.execute(statement=update_query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=ExperienceEntity.__name__)

    async def delete_experience(self, input_dto: DeleteExperienceCommandDTO) -> None:
        delete_query = (
            update(ExperienceEntity)
            .where(
                ExperienceEntity.experience_uuid == input_dto.experience_uuid,
                ExperienceEntity.is_deleted.is_(False),
            )
            .values(is_deleted=True)
        )

        result = await self._adapter.execute(statement=delete_query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=ExperienceEntity.__name__)

    async def create_honor(self, input_dto: CreateHonorCommandDTO) -> CreateHonorResponseDTO:
        _entity = HonorEntity(**input_dto.model_dump())
        result = await self._adapter.create(entity=_entity)
        return CreateHonorResponseDTO.model_validate(obj=result)

    async def get_honor(self, input_dto: GetHonorQueryDTO) -> GetHonorResponseDTO:
        select_query = select(HonorEntity).where(HonorEntity.is_deleted.is_(False))
        _query = self._apply_filter(
            query=select_query,
            field=HonorEntity.honor_uuid,
            value=input_dto.honor_uuid,
            operation=FilterOperationType.EQUAL,
        )
        result = await self._adapter.execute(statement=_query)
        entity = result.scalar()

        if not entity:
            raise NotFoundError(resource_type=HonorEntity.__name__)

        return GetHonorResponseDTO.model_validate(obj=entity)

    async def search_honors(self, input_dto: SearchHonorQueryDTO) -> SearchHonorResponseDTO:
        query: Select = select(HonorEntity).where(HonorEntity.is_deleted.is_(False))

        entities, total = await self._adapter.execute_search_query(
            query=query,
            entity=HonorEntity,
            sort_info=input_dto.sort_info,
            pagination=input_dto.pagination,
        )

        return SearchHonorResponseDTO(honors=entities, total=total)

    async def update_honor(self, input_dto: UpdateHonorCommandDTO) -> None:
        update_data = input_dto.model_dump(exclude={"honor_uuid"}, exclude_none=True)
        if not update_data:
            return

        update_query: Update = (
            update(HonorEntity)
            .where(
                HonorEntity.honor_uuid == input_dto.honor_uuid,
                HonorEntity.is_deleted.is_(False),
            )
            .values(**update_data)
        )

        result = await self._adapter.execute(statement=update_query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=HonorEntity.__name__)

    async def delete_honor(self, input_dto: DeleteHonorCommandDTO) -> None:
        delete_query = (
            update(HonorEntity)
            .where(
                HonorEntity.honor_uuid == input_dto.honor_uuid,
                HonorEntity.is_deleted.is_(False),
            )
            .values(is_deleted=True)
        )

        result = await self._adapter.execute(statement=delete_query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=HonorEntity.__name__)

    async def create_project(self, input_dto: CreateProjectCommandDTO) -> CreateProjectResponseDTO:
        _entity = ProjectEntity(**input_dto.model_dump())
        result = await self._adapter.create(entity=_entity)
        return CreateProjectResponseDTO.model_validate(obj=result)

    async def get_project(self, input_dto: GetProjectQueryDTO) -> GetProjectResponseDTO:
        select_query = select(ProjectEntity).where(ProjectEntity.is_deleted.is_(False))
        _query = self._apply_filter(
            query=select_query,
            field=ProjectEntity.project_uuid,
            value=input_dto.project_uuid,
            operation=FilterOperationType.EQUAL,
        )
        result = await self._adapter.execute(statement=_query)
        entity = result.scalar()

        if not entity:
            raise NotFoundError(resource_type=ProjectEntity.__name__)

        return GetProjectResponseDTO.model_validate(obj=entity)

    async def search_projects(self, input_dto: SearchProjectQueryDTO) -> SearchProjectResponseDTO:
        query: Select = select(ProjectEntity).where(ProjectEntity.is_deleted.is_(False))

        entities, total = await self._adapter.execute_search_query(
            query=query,
            entity=ProjectEntity,
            sort_info=input_dto.sort_info,
            pagination=input_dto.pagination,
        )

        return SearchProjectResponseDTO(projects=entities, total=total)

    async def update_project(self, input_dto: UpdateProjectCommandDTO) -> None:
        update_data = input_dto.model_dump(exclude={"project_uuid"}, exclude_none=True)
        if not update_data:
            return

        update_query: Update = (
            update(ProjectEntity)
            .where(
                ProjectEntity.project_uuid == input_dto.project_uuid,
                ProjectEntity.is_deleted.is_(False),
            )
            .values(**update_data)
        )

        result = await self._adapter.execute(statement=update_query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=ProjectEntity.__name__)

    async def delete_project(self, input_dto: DeleteProjectCommandDTO) -> None:
        delete_query = (
            update(ProjectEntity)
            .where(
                ProjectEntity.project_uuid == input_dto.project_uuid,
                ProjectEntity.is_deleted.is_(False),
            )
            .values(is_deleted=True)
        )

        result = await self._adapter.execute(statement=delete_query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=ProjectEntity.__name__)

    async def create_skill(self, input_dto: CreateSkillCommandDTO) -> CreateSkillResponseDTO:
        _entity = SkillEntity(**input_dto.model_dump())
        result = await self._adapter.create(entity=_entity)
        return CreateSkillResponseDTO.model_validate(obj=result)

    async def get_skill(self, input_dto: GetSkillQueryDTO) -> GetSkillResponseDTO:
        select_query = select(SkillEntity).where(SkillEntity.is_deleted.is_(False))
        _query = self._apply_filter(
            query=select_query,
            field=SkillEntity.skill_uuid,
            value=input_dto.skill_uuid,
            operation=FilterOperationType.EQUAL,
        )
        result = await self._adapter.execute(statement=_query)
        entity = result.scalar()

        if not entity:
            raise NotFoundError(resource_type=SkillEntity.__name__)

        return GetSkillResponseDTO.model_validate(obj=entity)

    async def search_skills(self, input_dto: SearchSkillQueryDTO) -> SearchSkillResponseDTO:
        query: Select = select(SkillEntity).where(SkillEntity.is_deleted.is_(False))

        entities, total = await self._adapter.execute_search_query(
            query=query,
            entity=SkillEntity,
            sort_info=input_dto.sort_info,
            pagination=input_dto.pagination,
        )

        return SearchSkillResponseDTO(skills=entities, total=total)

    async def update_skill(self, input_dto: UpdateSkillCommandDTO) -> None:
        update_data = input_dto.model_dump(exclude={"skill_uuid"}, exclude_none=True)
        if not update_data:
            return

        update_query: Update = (
            update(SkillEntity)
            .where(
                SkillEntity.skill_uuid == input_dto.skill_uuid,
                SkillEntity.is_deleted.is_(False),
            )
            .values(**update_data)
        )

        result = await self._adapter.execute(statement=update_query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=SkillEntity.__name__)

    async def delete_skill(self, input_dto: DeleteSkillCommandDTO) -> None:
        delete_query = (
            update(SkillEntity)
            .where(
                SkillEntity.skill_uuid == input_dto.skill_uuid,
                SkillEntity.is_deleted.is_(False),
            )
            .values(is_deleted=True)
        )

        result = await self._adapter.execute(statement=delete_query)
        if result.rowcount == 0:
            raise NotFoundError(resource_type=SkillEntity.__name__)
