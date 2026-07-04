from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.configs.containers import ServiceContainer
from src.logics.contact.contact_logic import ContactLogic
from src.models.dtos.contact.domain.v1.contact_domain_interface_dtos import (
    CreateContactMessageInputDTOV1,
    CreateContactMessageOutputDTOV1,
)
from src.models.types.api_router_type import ApiRouterType

routerV1: APIRouter = APIRouter(tags=[ApiRouterType.CONTACT])


@routerV1.post(
    path="/contact-messages",
    response_model=CreateContactMessageOutputDTOV1,
)
@inject
async def create_contact_message(
    input_dto: CreateContactMessageInputDTOV1,
    logic: ContactLogic = Depends(Provide[ServiceContainer.contact_logic]),
) -> CreateContactMessageOutputDTOV1:
    return await logic.create_contact_message(input_dto=input_dto)
