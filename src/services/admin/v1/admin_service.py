from uuid import UUID

from archipy.models.errors import NotFoundError
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.configs.containers import ServiceContainer
from src.logics.admin.admin_logic import AdminLogic
from src.logics.contact.contact_logic import ContactLogic
from src.logics.content.content_logic import ContentLogic
from src.models.dtos.admin.domain.v1.admin_domain_interface_dtos import (
    GetAdminInputDTOV1,
    GetAdminOutputDTOV1,
    SearchAdminOutputDTOV1,
)
from src.models.dtos.contact.domain.v1.contact_domain_interface_dtos import SearchContactMessageOutputDTOV1
from src.models.dtos.content.domain.v1.content_domain_interface_dtos import (
    CreateAboutOutputDTOV1,
    CreateExperienceInputDTOV1,
    CreateExperienceOutputDTOV1,
    CreateHonorInputDTOV1,
    CreateHonorOutputDTOV1,
    CreateProjectInputDTOV1,
    CreateProjectOutputDTOV1,
    CreateSkillInputDTOV1,
    CreateSkillOutputDTOV1,
    DeleteExperienceInputDTOV1,
    DeleteHonorInputDTOV1,
    DeleteProjectInputDTOV1,
    DeleteSkillInputDTOV1,
    UpdateExperienceInputDTOV1,
    UpdateExperienceRestInputDTOV1,
    UpdateHonorInputDTOV1,
    UpdateHonorRestInputDTOV1,
    UpdateProjectInputDTOV1,
    UpdateProjectRestInputDTOV1,
    UpdateSkillInputDTOV1,
    UpdateSkillRestInputDTOV1,
    CreateAboutInputDTOV1,
    UpdateAboutRestInputDTOV1,
    UpdateAboutInputDTOV1,
    DeleteAboutInputDTOV1,
)
from src.models.types.api_router_type import ApiRouterType
from src.utils.utils import Utils

routerV1: APIRouter = APIRouter(tags=[ApiRouterType.ADMIN])


@routerV1.get(
    path="/admins/{admin_uuid}",
    response_model=GetAdminOutputDTOV1,
    responses=Utils.get_fastapi_exception_responses([NotFoundError]),
)
@inject
async def get_admin(
    admin_uuid: UUID,
    logic: AdminLogic = Depends(Provide[ServiceContainer.admin_logic]),
) -> GetAdminOutputDTOV1:
    input_dto = GetAdminInputDTOV1(admin_uuid=admin_uuid)
    return await logic.get_admin(input_dto=input_dto)


@routerV1.get(
    path="/admins",
    response_model=SearchAdminOutputDTOV1,
)
@inject
async def search_admins(
    logic: AdminLogic = Depends(Provide[ServiceContainer.admin_logic]),
) -> SearchAdminOutputDTOV1:
    return await logic.search_admins()


@routerV1.post(
    path="/abouts",
    response_model=CreateAboutOutputDTOV1,
)
@inject
async def create_about(
    input_dto: CreateAboutInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> CreateAboutOutputDTOV1:
    return await logic.create_about(input_dto=input_dto)


@routerV1.put(
    path="/abouts/{about_uuid}",
)
@inject
async def update_about(
    about_uuid: UUID,
    input_dto: UpdateAboutRestInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    update_dto = UpdateAboutInputDTOV1(**input_dto.model_dump(), about_uuid=about_uuid)
    await logic.update_about(input_dto=update_dto)


@routerV1.delete(
    path="/abouts/{about_uuid}",
)
@inject
async def delete_about(
    about_uuid: UUID,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    input_dto = DeleteAboutInputDTOV1(about_uuid=about_uuid)
    await logic.delete_about(input_dto=input_dto)


@routerV1.post(
    path="/experiences",
    response_model=CreateExperienceOutputDTOV1,
)
@inject
async def create_experience(
    input_dto: CreateExperienceInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> CreateExperienceOutputDTOV1:
    return await logic.create_experience(input_dto=input_dto)


@routerV1.put(
    path="/experiences/{experience_uuid}",
)
@inject
async def update_experience(
    experience_uuid: UUID,
    input_dto: UpdateExperienceRestInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    update_dto = UpdateExperienceInputDTOV1(**input_dto.model_dump(), experience_uuid=experience_uuid)
    await logic.update_experience(input_dto=update_dto)


@routerV1.delete(
    path="/experiences/{experience_uuid}",
)
@inject
async def delete_experience(
    experience_uuid: UUID,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    input_dto = DeleteExperienceInputDTOV1(experience_uuid=experience_uuid)
    await logic.delete_experience(input_dto=input_dto)


@routerV1.post(
    path="/honors",
    response_model=CreateHonorOutputDTOV1,
)
@inject
async def create_honor(
    input_dto: CreateHonorInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> CreateHonorOutputDTOV1:
    return await logic.create_honor(input_dto=input_dto)


@routerV1.put(
    path="/honors/{honor_uuid}",
)
@inject
async def update_honor(
    honor_uuid: UUID,
    input_dto: UpdateHonorRestInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    update_dto = UpdateHonorInputDTOV1(**input_dto.model_dump(), honor_uuid=honor_uuid)
    await logic.update_honor(input_dto=update_dto)


@routerV1.delete(
    path="/honors/{honor_uuid}",
)
@inject
async def delete_honor(
    honor_uuid: UUID,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    input_dto = DeleteHonorInputDTOV1(honor_uuid=honor_uuid)
    await logic.delete_honor(input_dto=input_dto)


@routerV1.post(
    path="/projects",
    response_model=CreateProjectOutputDTOV1,
)
@inject
async def create_project(
    input_dto: CreateProjectInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> CreateProjectOutputDTOV1:
    return await logic.create_project(input_dto=input_dto)


@routerV1.put(
    path="/projects/{project_uuid}",
)
@inject
async def update_project(
    project_uuid: UUID,
    input_dto: UpdateProjectRestInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    update_dto = UpdateProjectInputDTOV1(**input_dto.model_dump(), project_uuid=project_uuid)
    await logic.update_project(input_dto=update_dto)


@routerV1.delete(
    path="/projects/{project_uuid}",
)
@inject
async def delete_project(
    project_uuid: UUID,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    input_dto = DeleteProjectInputDTOV1(project_uuid=project_uuid)
    await logic.delete_project(input_dto=input_dto)


@routerV1.post(
    path="/skills",
    response_model=CreateSkillOutputDTOV1,
)
@inject
async def create_skill(
    input_dto: CreateSkillInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> CreateSkillOutputDTOV1:
    return await logic.create_skill(input_dto=input_dto)


@routerV1.put(
    path="/skills/{skill_uuid}",
)
@inject
async def update_skill(
    skill_uuid: UUID,
    input_dto: UpdateSkillRestInputDTOV1,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    update_dto = UpdateSkillInputDTOV1(**input_dto.model_dump(), skill_uuid=skill_uuid)
    await logic.update_skill(input_dto=update_dto)


@routerV1.delete(
    path="/skills/{skill_uuid}",
)
@inject
async def delete_skill(
    skill_uuid: UUID,
    logic: ContentLogic = Depends(Provide[ServiceContainer.content_logic]),
) -> None:
    input_dto = DeleteSkillInputDTOV1(skill_uuid=skill_uuid)
    await logic.delete_skill(input_dto=input_dto)


@routerV1.get(
    path="/contact-messages",
    response_model=SearchContactMessageOutputDTOV1,
)
@inject
async def search_contact_messages(
    logic: ContactLogic = Depends(Provide[ServiceContainer.contact_logic]),
) -> SearchContactMessageOutputDTOV1:
    return await logic.search_contact_messages()
