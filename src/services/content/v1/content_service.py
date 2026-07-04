from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.configs.containers import ServiceContainer
from src.logics.content.content_logic import ContentLogic
from src.models.dtos.content.domain.v1.content_domain_interface_dtos import (
    SearchAboutOutputDTOV1,
    SearchExperienceOutputDTOV1,
    SearchHonorOutputDTOV1,
    SearchProjectOutputDTOV1,
    SearchSkillOutputDTOV1,
)
from src.models.types.api_router_type import ApiRouterType

routerV1: APIRouter = APIRouter(tags=[ApiRouterType.CONTENT])


@routerV1.get(
    path="/abouts",
    response_model=SearchAboutOutputDTOV1,
)
@inject
async def search_abouts(
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> SearchAboutOutputDTOV1:
    return await logic.search_abouts()


@routerV1.get(
    path="/experiences",
    response_model=SearchExperienceOutputDTOV1,
)
@inject
async def search_experiences(
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> SearchExperienceOutputDTOV1:
    return await logic.search_experiences()


@routerV1.get(
    path="/honors",
    response_model=SearchHonorOutputDTOV1,
)
@inject
async def search_honors(
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> SearchHonorOutputDTOV1:
    return await logic.search_honors()


@routerV1.get(
    path="/projects",
    response_model=SearchProjectOutputDTOV1,
)
@inject
async def search_projects(
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> SearchProjectOutputDTOV1:
    return await logic.search_projects()


@routerV1.get(
    path="/skills",
    response_model=SearchSkillOutputDTOV1,
)
@inject
async def search_skills(
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> SearchSkillOutputDTOV1:
    return await logic.search_skills()
