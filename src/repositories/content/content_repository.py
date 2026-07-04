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
from src.repositories.content.adapters.content_postgres_adapter import ContentPostgresAdapter


class ContentRepository:
    def __init__(self, postgres_adapter: ContentPostgresAdapter):
        self._postgres_adapter: ContentPostgresAdapter = postgres_adapter

    async def create_about(self, input_dto: CreateAboutCommandDTO) -> CreateAboutResponseDTO:
        return await self._postgres_adapter.create_about(input_dto=input_dto)

    async def get_about(self, input_dto: GetAboutQueryDTO) -> GetAboutResponseDTO:
        return await self._postgres_adapter.get_about(input_dto=input_dto)

    async def search_abouts(self, input_dto: SearchAboutQueryDTO) -> SearchAboutResponseDTO:
        return await self._postgres_adapter.search_abouts(input_dto=input_dto)

    async def update_about(self, input_dto: UpdateAboutCommandDTO) -> None:
        await self._postgres_adapter.update_about(input_dto=input_dto)

    async def delete_about(self, input_dto: DeleteAboutCommandDTO) -> None:
        await self._postgres_adapter.delete_about(input_dto=input_dto)

    async def create_experience(self, input_dto: CreateExperienceCommandDTO) -> CreateExperienceResponseDTO:
        return await self._postgres_adapter.create_experience(input_dto=input_dto)

    async def get_experience(self, input_dto: GetExperienceQueryDTO) -> GetExperienceResponseDTO:
        return await self._postgres_adapter.get_experience(input_dto=input_dto)

    async def search_experiences(self, input_dto: SearchExperienceQueryDTO) -> SearchExperienceResponseDTO:
        return await self._postgres_adapter.search_experiences(input_dto=input_dto)

    async def update_experience(self, input_dto: UpdateExperienceCommandDTO) -> None:
        await self._postgres_adapter.update_experience(input_dto=input_dto)

    async def delete_experience(self, input_dto: DeleteExperienceCommandDTO) -> None:
        await self._postgres_adapter.delete_experience(input_dto=input_dto)

    async def create_honor(self, input_dto: CreateHonorCommandDTO) -> CreateHonorResponseDTO:
        return await self._postgres_adapter.create_honor(input_dto=input_dto)

    async def get_honor(self, input_dto: GetHonorQueryDTO) -> GetHonorResponseDTO:
        return await self._postgres_adapter.get_honor(input_dto=input_dto)

    async def search_honors(self, input_dto: SearchHonorQueryDTO) -> SearchHonorResponseDTO:
        return await self._postgres_adapter.search_honors(input_dto=input_dto)

    async def update_honor(self, input_dto: UpdateHonorCommandDTO) -> None:
        await self._postgres_adapter.update_honor(input_dto=input_dto)

    async def delete_honor(self, input_dto: DeleteHonorCommandDTO) -> None:
        await self._postgres_adapter.delete_honor(input_dto=input_dto)

    async def create_project(self, input_dto: CreateProjectCommandDTO) -> CreateProjectResponseDTO:
        return await self._postgres_adapter.create_project(input_dto=input_dto)

    async def get_project(self, input_dto: GetProjectQueryDTO) -> GetProjectResponseDTO:
        return await self._postgres_adapter.get_project(input_dto=input_dto)

    async def search_projects(self, input_dto: SearchProjectQueryDTO) -> SearchProjectResponseDTO:
        return await self._postgres_adapter.search_projects(input_dto=input_dto)

    async def update_project(self, input_dto: UpdateProjectCommandDTO) -> None:
        await self._postgres_adapter.update_project(input_dto=input_dto)

    async def delete_project(self, input_dto: DeleteProjectCommandDTO) -> None:
        await self._postgres_adapter.delete_project(input_dto=input_dto)

    async def create_skill(self, input_dto: CreateSkillCommandDTO) -> CreateSkillResponseDTO:
        return await self._postgres_adapter.create_skill(input_dto=input_dto)

    async def get_skill(self, input_dto: GetSkillQueryDTO) -> GetSkillResponseDTO:
        return await self._postgres_adapter.get_skill(input_dto=input_dto)

    async def search_skills(self, input_dto: SearchSkillQueryDTO) -> SearchSkillResponseDTO:
        return await self._postgres_adapter.search_skills(input_dto=input_dto)

    async def update_skill(self, input_dto: UpdateSkillCommandDTO) -> None:
        await self._postgres_adapter.update_skill(input_dto=input_dto)

    async def delete_skill(self, input_dto: DeleteSkillCommandDTO) -> None:
        await self._postgres_adapter.delete_skill(input_dto=input_dto)
