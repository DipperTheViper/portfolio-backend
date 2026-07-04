from archipy.adapters.base.sqlalchemy.adapters import SQLAlchemyFilterMixin
from archipy.adapters.postgres.sqlalchemy.adapters import AsyncPostgresSQLAlchemyAdapter
from archipy.models.errors import NotFoundError
from sqlalchemy import select, update
from sqlalchemy.sql.expression import Select, Update

from src.models.dtos.content.repository.content_repository_interface_dtos import (
    CreateAboutCommandDTO,
    CreateAboutResponseDTO,
    UpdateAboutCommandDTO,
    DeleteAboutCommandDTO,
    SearchAboutResponseDTO,
    CreateExperienceCommandDTO,
    CreateExperienceResponseDTO,
    UpdateExperienceCommandDTO,
    DeleteExperienceCommandDTO,
    SearchExperienceResponseDTO,
    CreateHonorCommandDTO,
    CreateHonorResponseDTO,
    UpdateHonorCommandDTO,
    DeleteHonorCommandDTO,
    SearchHonorResponseDTO,
    CreateProjectCommandDTO,
    CreateProjectResponseDTO,
    UpdateProjectCommandDTO,
    DeleteProjectCommandDTO,
    SearchProjectResponseDTO,
    CreateSkillCommandDTO,
    CreateSkillResponseDTO,
    UpdateSkillCommandDTO,
    DeleteSkillCommandDTO,
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

    async def search_abouts(self) -> SearchAboutResponseDTO:
        query: Select = select(AboutEntity).where(AboutEntity.is_deleted.is_(False))

        entities, total = await self._adapter.execute_search_query(
            query=query,
            entity=AboutEntity,
            sort_info=None,
            pagination=None,
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

    async def search_experiences(self) -> SearchExperienceResponseDTO:
        query: Select = select(ExperienceEntity).where(ExperienceEntity.is_deleted.is_(False))

        entities, total = await self._adapter.execute_search_query(
            query=query,
            entity=ExperienceEntity,
            sort_info=None,
            pagination=None,
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

    async def search_honors(self) -> SearchHonorResponseDTO:
        query: Select = select(HonorEntity).where(HonorEntity.is_deleted.is_(False))

        entities, total = await self._adapter.execute_search_query(
            query=query,
            entity=HonorEntity,
            sort_info=None,
            pagination=None,
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

    async def search_projects(self) -> SearchProjectResponseDTO:
        query: Select = select(ProjectEntity).where(ProjectEntity.is_deleted.is_(False))

        entities, total = await self._adapter.execute_search_query(
            query=query,
            entity=ProjectEntity,
            sort_info=None,
            pagination=None,
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

    async def search_skills(self) -> SearchSkillResponseDTO:
        query: Select = select(SkillEntity).where(SkillEntity.is_deleted.is_(False))

        entities, total = await self._adapter.execute_search_query(
            query=query,
            entity=SkillEntity,
            sort_info=None,
            pagination=None,
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
