from archipy.helpers.decorators.sqlalchemy_atomic import async_postgres_sqlalchemy_atomic_decorator

from src.models.dtos.content.domain.v1.content_domain_interface_dtos import (
    CreateAboutInputDTOV1,
    CreateAboutOutputDTOV1,
    UpdateAboutInputDTOV1,
    DeleteAboutInputDTOV1,
    SearchAboutOutputDTOV1,
    CreateExperienceInputDTOV1,
    CreateExperienceOutputDTOV1,
    UpdateExperienceInputDTOV1,
    DeleteExperienceInputDTOV1,
    SearchExperienceOutputDTOV1,
    CreateHonorInputDTOV1,
    CreateHonorOutputDTOV1,
    UpdateHonorInputDTOV1,
    DeleteHonorInputDTOV1,
    SearchHonorOutputDTOV1,
    CreateProjectInputDTOV1,
    CreateProjectOutputDTOV1,
    UpdateProjectInputDTOV1,
    DeleteProjectInputDTOV1,
    SearchProjectOutputDTOV1,
    CreateSkillInputDTOV1,
    CreateSkillOutputDTOV1,
    UpdateSkillInputDTOV1,
    DeleteSkillInputDTOV1,
    SearchSkillOutputDTOV1,
)
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
from src.repositories.content.content_repository import ContentRepository


class ContentLogic:
    def __init__(
        self,
        repository: ContentRepository,
    ) -> None:
        self._repository: ContentRepository = repository

    @async_postgres_sqlalchemy_atomic_decorator
    async def create_about(self, input_dto: CreateAboutInputDTOV1) -> CreateAboutOutputDTOV1:
        command = CreateAboutCommandDTO.model_validate(input_dto)
        response: CreateAboutResponseDTO = await self._repository.create_about(input_dto=command)
        return CreateAboutOutputDTOV1.model_validate(obj=response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def search_abouts(self) -> SearchAboutOutputDTOV1:
        response: SearchAboutResponseDTO = await self._repository.search_abouts()
        return SearchAboutOutputDTOV1.model_validate(response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def update_about(self, input_dto: UpdateAboutInputDTOV1) -> None:
        command = UpdateAboutCommandDTO.model_validate(obj=input_dto)
        await self._repository.update_about(input_dto=command)

    @async_postgres_sqlalchemy_atomic_decorator
    async def delete_about(self, input_dto: DeleteAboutInputDTOV1) -> None:
        command = DeleteAboutCommandDTO.model_validate(obj=input_dto)
        await self._repository.delete_about(input_dto=command)

    @async_postgres_sqlalchemy_atomic_decorator
    async def create_experience(self, input_dto: CreateExperienceInputDTOV1) -> CreateExperienceOutputDTOV1:
        command = CreateExperienceCommandDTO.model_validate(input_dto)
        response: CreateExperienceResponseDTO = await self._repository.create_experience(input_dto=command)
        return CreateExperienceOutputDTOV1.model_validate(obj=response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def search_experiences(self) -> SearchExperienceOutputDTOV1:
        response: SearchExperienceResponseDTO = await self._repository.search_experiences()
        return SearchExperienceOutputDTOV1.model_validate(response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def update_experience(self, input_dto: UpdateExperienceInputDTOV1) -> None:
        command = UpdateExperienceCommandDTO.model_validate(obj=input_dto)
        await self._repository.update_experience(input_dto=command)

    @async_postgres_sqlalchemy_atomic_decorator
    async def delete_experience(self, input_dto: DeleteExperienceInputDTOV1) -> None:
        command = DeleteExperienceCommandDTO.model_validate(obj=input_dto)
        await self._repository.delete_experience(input_dto=command)

    @async_postgres_sqlalchemy_atomic_decorator
    async def create_honor(self, input_dto: CreateHonorInputDTOV1) -> CreateHonorOutputDTOV1:
        command = CreateHonorCommandDTO.model_validate(input_dto)
        response: CreateHonorResponseDTO = await self._repository.create_honor(input_dto=command)
        return CreateHonorOutputDTOV1.model_validate(obj=response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def search_honors(self) -> SearchHonorOutputDTOV1:
        response: SearchHonorResponseDTO = await self._repository.search_honors()
        return SearchHonorOutputDTOV1.model_validate(response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def update_honor(self, input_dto: UpdateHonorInputDTOV1) -> None:
        command = UpdateHonorCommandDTO.model_validate(obj=input_dto)
        await self._repository.update_honor(input_dto=command)

    @async_postgres_sqlalchemy_atomic_decorator
    async def delete_honor(self, input_dto: DeleteHonorInputDTOV1) -> None:
        command = DeleteHonorCommandDTO.model_validate(obj=input_dto)
        await self._repository.delete_honor(input_dto=command)

    @async_postgres_sqlalchemy_atomic_decorator
    async def create_project(self, input_dto: CreateProjectInputDTOV1) -> CreateProjectOutputDTOV1:
        command = CreateProjectCommandDTO.model_validate(input_dto)
        response: CreateProjectResponseDTO = await self._repository.create_project(input_dto=command)
        return CreateProjectOutputDTOV1.model_validate(obj=response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def search_projects(self) -> SearchProjectOutputDTOV1:
        response: SearchProjectResponseDTO = await self._repository.search_projects()
        return SearchProjectOutputDTOV1.model_validate(response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def update_project(self, input_dto: UpdateProjectInputDTOV1) -> None:
        command = UpdateProjectCommandDTO.model_validate(obj=input_dto)
        await self._repository.update_project(input_dto=command)

    @async_postgres_sqlalchemy_atomic_decorator
    async def delete_project(self, input_dto: DeleteProjectInputDTOV1) -> None:
        command = DeleteProjectCommandDTO.model_validate(obj=input_dto)
        await self._repository.delete_project(input_dto=command)

    @async_postgres_sqlalchemy_atomic_decorator
    async def create_skill(self, input_dto: CreateSkillInputDTOV1) -> CreateSkillOutputDTOV1:
        command = CreateSkillCommandDTO.model_validate(input_dto)
        response: CreateSkillResponseDTO = await self._repository.create_skill(input_dto=command)
        return CreateSkillOutputDTOV1.model_validate(obj=response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def search_skills(self) -> SearchSkillOutputDTOV1:
        response: SearchSkillResponseDTO = await self._repository.search_skills()
        return SearchSkillOutputDTOV1.model_validate(response)

    @async_postgres_sqlalchemy_atomic_decorator
    async def update_skill(self, input_dto: UpdateSkillInputDTOV1) -> None:
        command = UpdateSkillCommandDTO.model_validate(obj=input_dto)
        await self._repository.update_skill(input_dto=command)

    @async_postgres_sqlalchemy_atomic_decorator
    async def delete_skill(self, input_dto: DeleteSkillInputDTOV1) -> None:
        command = DeleteSkillCommandDTO.model_validate(obj=input_dto)
        await self._repository.delete_skill(input_dto=command)
