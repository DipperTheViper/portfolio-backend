from archipy.helpers.interceptors.fastapi.rate_limit.fastapi_rest_rate_limit_handler import FastAPIRestRateLimitHandler
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Body

from src.configs.containers import ServiceContainer
from src.configs.runtime_config import RuntimeConfig
from src.logics.auth.auth_logic import AuthLogic
from src.models.dtos.auth.domain_interface.v1.auth_domain_interface_dtos import (
    LoginOutputDTOV1,
    LoginInputDTOV1,
)
from src.models.types.api_router_type import ApiRouterType

routerV1 = APIRouter(tags=[ApiRouterType.ADMIN_AUTH])


@routerV1.post(
    path="/login",
    response_model=LoginOutputDTOV1,
    dependencies=[
        Depends(
            FastAPIRestRateLimitHandler(
                calls_count=RuntimeConfig.global_config().ADMIN_AUTH_LOGIN_CALLS_COUNT_LIMIT,
                minutes=RuntimeConfig.global_config().ADMIN_AUTH_LOGIN_MINUTES_LIMIT,
            ),
        ),
    ],
)
@inject
async def login(
    data: LoginInputDTOV1 = Body(default={"username": "admin", "password": "1234"}),
    auth_logic: AuthLogic = Depends(Provide[ServiceContainer.auth_logic]),
) -> LoginOutputDTOV1:
    return await auth_logic.login(input_dto=data)
