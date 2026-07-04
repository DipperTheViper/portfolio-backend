from archipy.models.errors import NotFoundError
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Query
from uuid import UUID

from src.configs.containers import ServiceContainer
from src.logics.content.content_logic import ContentLogic
from src.models.dtos.content.domain.v1.content_domain_interface_dtos import (
    CreateAboutInputDTOV1, CreateAboutOutputDTOV1, CreateAboutRestInputDTOV1, CreateExperienceInputDTOV1, CreateExperienceOutputDTOV1, CreateExperienceRestInputDTOV1, CreateHonorInputDTOV1, CreateHonorOutputDTOV1, CreateHonorRestInputDTOV1, CreateProjectInputDTOV1, CreateProjectOutputDTOV1, CreateProjectRestInputDTOV1, CreateSkillInputDTOV1, CreateSkillOutputDTOV1, CreateSkillRestInputDTOV1, DeleteAboutInputDTOV1, DeleteExperienceInputDTOV1, DeleteHonorInputDTOV1, DeleteProjectInputDTOV1, DeleteSkillInputDTOV1, GetAboutInputDTOV1, GetAboutOutputDTOV1, GetExperienceInputDTOV1, GetExperienceOutputDTOV1, GetHonorInputDTOV1, GetHonorOutputDTOV1, GetProjectInputDTOV1, GetProjectOutputDTOV1, GetSkillInputDTOV1, GetSkillOutputDTOV1, SearchAboutInputDTOV1, SearchAboutOutputDTOV1, SearchExperienceInputDTOV1, SearchExperienceOutputDTOV1, SearchHonorInputDTOV1, SearchHonorOutputDTOV1, SearchProjectInputDTOV1, SearchProjectOutputDTOV1, SearchSkillInputDTOV1, SearchSkillOutputDTOV1, UpdateAboutInputDTOV1, UpdateAboutRestInputDTOV1, UpdateExperienceInputDTOV1, UpdateExperienceRestInputDTOV1, UpdateHonorInputDTOV1, UpdateHonorRestInputDTOV1, UpdateProjectInputDTOV1, UpdateProjectRestInputDTOV1, UpdateSkillInputDTOV1, UpdateSkillRestInputDTOV1
)
from src.models.types.api_router_type import ApiRouterType
from src.utils.utils import Utils

routerV1: APIRouter = APIRouter(tags=[ApiRouterType.CONTENT])



@routerV1.post(
    path="/{user_uuid}/abouts",
    response_model=CreateAboutOutputDTOV1,
)
@inject
async def create_about(
    user_uuid: UUID,
    input_dto: CreateAboutRestInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> CreateAboutOutputDTOV1:
    input_dto = CreateAboutInputDTOV1.create(user_uuid=user_uuid, input_dto=input_dto)
    return await logic.create_about(input_dto=input_dto)


@routerV1.get(
    path="/{user_uuid}/abouts/{about_uuid}",
    response_model=GetAboutOutputDTOV1,
    responses=Utils.get_fastapi_exception_responses([NotFoundError]),
)
@inject
async def get_about(
    user_uuid: UUID,
    about_uuid: UUID,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> GetAboutOutputDTOV1:
    input_dto = GetAboutInputDTOV1(about_uuid=about_uuid)
    return await logic.get_about(input_dto=input_dto)


@routerV1.get(
    path="/{user_uuid}/abouts",
    response_model=SearchAboutOutputDTOV1,
)
@inject
async def search_abouts(
    user_uuid: UUID,
    page: int = Query(default=1, ge=1, description="Page number"),
    page_size: int = Query(default=10, ge=1, le=100, description="Number of items per page"),
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> SearchAboutOutputDTOV1:
    input_dto = SearchAboutInputDTOV1.create(
        page=page,
        page_size=page_size,
    )
    return await logic.search_abouts(input_dto=input_dto)


@routerV1.put(
    path="/{user_uuid}/abouts/{about_uuid}",
)
@inject
async def update_about(
    user_uuid: UUID,
    about_uuid: UUID,
    input_dto: UpdateAboutRestInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    update_dto = UpdateAboutInputDTOV1(**input_dto.model_dump(), about_uuid=about_uuid)
    await logic.update_about(input_dto=update_dto)


@routerV1.delete(
    path="/{user_uuid}/abouts/{about_uuid}",
)
@inject
async def delete_about(
    user_uuid: UUID,
    about_uuid: UUID,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    input_dto = DeleteAboutInputDTOV1(about_uuid=about_uuid)
    await logic.delete_about(input_dto=input_dto)



@routerV1.post(
    path="/{user_uuid}/experiences",
    response_model=CreateExperienceOutputDTOV1,
)
@inject
async def create_experience(
    user_uuid: UUID,
    input_dto: CreateExperienceRestInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> CreateExperienceOutputDTOV1:
    input_dto = CreateExperienceInputDTOV1.create(user_uuid=user_uuid, input_dto=input_dto)
    return await logic.create_experience(input_dto=input_dto)


@routerV1.get(
    path="/{user_uuid}/experiences/{experience_uuid}",
    response_model=GetExperienceOutputDTOV1,
    responses=Utils.get_fastapi_exception_responses([NotFoundError]),
)
@inject
async def get_experience(
    user_uuid: UUID,
    experience_uuid: UUID,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> GetExperienceOutputDTOV1:
    input_dto = GetExperienceInputDTOV1(experience_uuid=experience_uuid)
    return await logic.get_experience(input_dto=input_dto)


@routerV1.get(
    path="/{user_uuid}/experiences",
    response_model=SearchExperienceOutputDTOV1,
)
@inject
async def search_experiences(
    user_uuid: UUID,
    page: int = Query(default=1, ge=1, description="Page number"),
    page_size: int = Query(default=10, ge=1, le=100, description="Number of items per page"),
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> SearchExperienceOutputDTOV1:
    input_dto = SearchExperienceInputDTOV1.create(
        page=page,
        page_size=page_size,
    )
    return await logic.search_experiences(input_dto=input_dto)


@routerV1.put(
    path="/{user_uuid}/experiences/{experience_uuid}",
)
@inject
async def update_experience(
    user_uuid: UUID,
    experience_uuid: UUID,
    input_dto: UpdateExperienceRestInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    update_dto = UpdateExperienceInputDTOV1(**input_dto.model_dump(), experience_uuid=experience_uuid)
    await logic.update_experience(input_dto=update_dto)


@routerV1.delete(
    path="/{user_uuid}/experiences/{experience_uuid}",
)
@inject
async def delete_experience(
    user_uuid: UUID,
    experience_uuid: UUID,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    input_dto = DeleteExperienceInputDTOV1(experience_uuid=experience_uuid)
    await logic.delete_experience(input_dto=input_dto)



@routerV1.post(
    path="/{user_uuid}/honors",
    response_model=CreateHonorOutputDTOV1,
)
@inject
async def create_honor(
    user_uuid: UUID,
    input_dto: CreateHonorRestInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> CreateHonorOutputDTOV1:
    input_dto = CreateHonorInputDTOV1.create(user_uuid=user_uuid, input_dto=input_dto)
    return await logic.create_honor(input_dto=input_dto)


@routerV1.get(
    path="/{user_uuid}/honors/{honor_uuid}",
    response_model=GetHonorOutputDTOV1,
    responses=Utils.get_fastapi_exception_responses([NotFoundError]),
)
@inject
async def get_honor(
    user_uuid: UUID,
    honor_uuid: UUID,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> GetHonorOutputDTOV1:
    input_dto = GetHonorInputDTOV1(honor_uuid=honor_uuid)
    return await logic.get_honor(input_dto=input_dto)


@routerV1.get(
    path="/{user_uuid}/honors",
    response_model=SearchHonorOutputDTOV1,
)
@inject
async def search_honors(
    user_uuid: UUID,
    page: int = Query(default=1, ge=1, description="Page number"),
    page_size: int = Query(default=10, ge=1, le=100, description="Number of items per page"),
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> SearchHonorOutputDTOV1:
    input_dto = SearchHonorInputDTOV1.create(
        page=page,
        page_size=page_size,
    )
    return await logic.search_honors(input_dto=input_dto)


@routerV1.put(
    path="/{user_uuid}/honors/{honor_uuid}",
)
@inject
async def update_honor(
    user_uuid: UUID,
    honor_uuid: UUID,
    input_dto: UpdateHonorRestInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    update_dto = UpdateHonorInputDTOV1(**input_dto.model_dump(), honor_uuid=honor_uuid)
    await logic.update_honor(input_dto=update_dto)


@routerV1.delete(
    path="/{user_uuid}/honors/{honor_uuid}",
)
@inject
async def delete_honor(
    user_uuid: UUID,
    honor_uuid: UUID,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    input_dto = DeleteHonorInputDTOV1(honor_uuid=honor_uuid)
    await logic.delete_honor(input_dto=input_dto)



@routerV1.post(
    path="/{user_uuid}/projects",
    response_model=CreateProjectOutputDTOV1,
)
@inject
async def create_project(
    user_uuid: UUID,
    input_dto: CreateProjectRestInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> CreateProjectOutputDTOV1:
    input_dto = CreateProjectInputDTOV1.create(user_uuid=user_uuid, input_dto=input_dto)
    return await logic.create_project(input_dto=input_dto)


@routerV1.get(
    path="/{user_uuid}/projects/{project_uuid}",
    response_model=GetProjectOutputDTOV1,
    responses=Utils.get_fastapi_exception_responses([NotFoundError]),
)
@inject
async def get_project(
    user_uuid: UUID,
    project_uuid: UUID,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> GetProjectOutputDTOV1:
    input_dto = GetProjectInputDTOV1(project_uuid=project_uuid)
    return await logic.get_project(input_dto=input_dto)


@routerV1.get(
    path="/{user_uuid}/projects",
    response_model=SearchProjectOutputDTOV1,
)
@inject
async def search_projects(
    user_uuid: UUID,
    page: int = Query(default=1, ge=1, description="Page number"),
    page_size: int = Query(default=10, ge=1, le=100, description="Number of items per page"),
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> SearchProjectOutputDTOV1:
    input_dto = SearchProjectInputDTOV1.create(
        page=page,
        page_size=page_size,
    )
    return await logic.search_projects(input_dto=input_dto)


@routerV1.put(
    path="/{user_uuid}/projects/{project_uuid}",
)
@inject
async def update_project(
    user_uuid: UUID,
    project_uuid: UUID,
    input_dto: UpdateProjectRestInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    update_dto = UpdateProjectInputDTOV1(**input_dto.model_dump(), project_uuid=project_uuid)
    await logic.update_project(input_dto=update_dto)


@routerV1.delete(
    path="/{user_uuid}/projects/{project_uuid}",
)
@inject
async def delete_project(
    user_uuid: UUID,
    project_uuid: UUID,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    input_dto = DeleteProjectInputDTOV1(project_uuid=project_uuid)
    await logic.delete_project(input_dto=input_dto)



@routerV1.post(
    path="/{user_uuid}/skills",
    response_model=CreateSkillOutputDTOV1,
)
@inject
async def create_skill(
    user_uuid: UUID,
    input_dto: CreateSkillRestInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> CreateSkillOutputDTOV1:
    input_dto = CreateSkillInputDTOV1.create(user_uuid=user_uuid, input_dto=input_dto)
    return await logic.create_skill(input_dto=input_dto)


@routerV1.get(
    path="/{user_uuid}/skills/{skill_uuid}",
    response_model=GetSkillOutputDTOV1,
    responses=Utils.get_fastapi_exception_responses([NotFoundError]),
)
@inject
async def get_skill(
    user_uuid: UUID,
    skill_uuid: UUID,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> GetSkillOutputDTOV1:
    input_dto = GetSkillInputDTOV1(skill_uuid=skill_uuid)
    return await logic.get_skill(input_dto=input_dto)


@routerV1.get(
    path="/{user_uuid}/skills",
    response_model=SearchSkillOutputDTOV1,
)
@inject
async def search_skills(
    user_uuid: UUID,
    page: int = Query(default=1, ge=1, description="Page number"),
    page_size: int = Query(default=10, ge=1, le=100, description="Number of items per page"),
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> SearchSkillOutputDTOV1:
    input_dto = SearchSkillInputDTOV1.create(
        page=page,
        page_size=page_size,
    )
    return await logic.search_skills(input_dto=input_dto)


@routerV1.put(
    path="/{user_uuid}/skills/{skill_uuid}",
)
@inject
async def update_skill(
    user_uuid: UUID,
    skill_uuid: UUID,
    input_dto: UpdateSkillRestInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    update_dto = UpdateSkillInputDTOV1(**input_dto.model_dump(), skill_uuid=skill_uuid)
    await logic.update_skill(input_dto=update_dto)


@routerV1.delete(
    path="/{user_uuid}/skills/{skill_uuid}",
)
@inject
async def delete_skill(
    user_uuid: UUID,
    skill_uuid: UUID,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    input_dto = DeleteSkillInputDTOV1(skill_uuid=skill_uuid)
    await logic.delete_skill(input_dto=input_dto)

