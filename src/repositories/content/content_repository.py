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
from src.repositories.content.adapters.content_postgres_adapter import ContentPostgresAdapter


class ContentRepository:
    def __init__(self, postgres_adapter: ContentPostgresAdapter):
        self._postgres_adapter: ContentPostgresAdapter = postgres_adapter

    async def create_about(self, input_dto: CreateAboutCommandDTO) -> CreateAboutResponseDTO:
        return await self._postgres_adapter.create_about(input_dto=input_dto)

    async def search_abouts(self) -> SearchAboutResponseDTO:
        return await self._postgres_adapter.search_abouts()

    async def update_about(self, input_dto: UpdateAboutCommandDTO) -> None:
        await self._postgres_adapter.update_about(input_dto=input_dto)

    async def delete_about(self, input_dto: DeleteAboutCommandDTO) -> None:
        await self._postgres_adapter.delete_about(input_dto=input_dto)

    async def create_experience(self, input_dto: CreateExperienceCommandDTO) -> CreateExperienceResponseDTO:
        return await self._postgres_adapter.create_experience(input_dto=input_dto)

    async def search_experiences(self) -> SearchExperienceResponseDTO:
        return await self._postgres_adapter.search_experiences()

    async def update_experience(self, input_dto: UpdateExperienceCommandDTO) -> None:
        await self._postgres_adapter.update_experience(input_dto=input_dto)

    async def delete_experience(self, input_dto: DeleteExperienceCommandDTO) -> None:
        await self._postgres_adapter.delete_experience(input_dto=input_dto)

    async def create_honor(self, input_dto: CreateHonorCommandDTO) -> CreateHonorResponseDTO:
        return await self._postgres_adapter.create_honor(input_dto=input_dto)

    async def search_honors(self) -> SearchHonorResponseDTO:
        return await self._postgres_adapter.search_honors()

    async def update_honor(self, input_dto: UpdateHonorCommandDTO) -> None:
        await self._postgres_adapter.update_honor(input_dto=input_dto)

    async def delete_honor(self, input_dto: DeleteHonorCommandDTO) -> None:
        await self._postgres_adapter.delete_honor(input_dto=input_dto)

    async def create_project(self, input_dto: CreateProjectCommandDTO) -> CreateProjectResponseDTO:
        return await self._postgres_adapter.create_project(input_dto=input_dto)

    async def search_projects(self) -> SearchProjectResponseDTO:
        return await self._postgres_adapter.search_projects()

    async def update_project(self, input_dto: UpdateProjectCommandDTO) -> None:
        await self._postgres_adapter.update_project(input_dto=input_dto)

    async def delete_project(self, input_dto: DeleteProjectCommandDTO) -> None:
        await self._postgres_adapter.delete_project(input_dto=input_dto)

    async def create_skill(self, input_dto: CreateSkillCommandDTO) -> CreateSkillResponseDTO:
        return await self._postgres_adapter.create_skill(input_dto=input_dto)

    async def search_skills(self) -> SearchSkillResponseDTO:
        return await self._postgres_adapter.search_skills()

    async def update_skill(self, input_dto: UpdateSkillCommandDTO) -> None:
        await self._postgres_adapter.update_skill(input_dto=input_dto)

    async def delete_skill(self, input_dto: DeleteSkillCommandDTO) -> None:
        await self._postgres_adapter.delete_skill(input_dto=input_dto)
