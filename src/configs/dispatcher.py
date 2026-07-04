from archipy.helpers.utils.base_utils import BaseUtils
from archipy.models.errors import UnauthenticatedError, UnknownError, UnavailableError, InvalidArgumentError
from fastapi import Depends, FastAPI

from src.configs.containers import ServiceContainer
from src.logics.auth.admin_authenticator_logic import AdminAuthenticator
from src.services.admin.v1 import admin_service
from src.services.auth.v1 import auth_service
from src.services.contact.v1 import contact_service
from src.services.content.v1 import content_service
from src.services.file.v1 import file_service


def set_dispatch_routes(app: FastAPI) -> None:
    # TODO: wire up public/user authentication once that feature is built.
    common_private_response = BaseUtils.get_fastapi_exception_responses(
        [UnauthenticatedError, UnknownError, UnavailableError, InvalidArgumentError],
    )

    app.include_router(
        router=contact_service.routerV1,
        prefix="/api/v1/users",
        responses=common_private_response,
    )

    app.include_router(
        router=content_service.routerV1,
        prefix="/api/v1/users",
        responses=common_private_response,
    )

    app.include_router(
        router=file_service.routerV1,
        prefix="/api/v1/users",
        responses=common_private_response,
    )


def set_admin_dispatch_routes(app: FastAPI) -> None:
    admin_authenticator = AdminAuthenticator(admin_logic=ServiceContainer.admin_logic())
    common_private_response = BaseUtils.get_fastapi_exception_responses(
        [UnauthenticatedError, UnknownError, UnavailableError, InvalidArgumentError],
    )

    app.include_router(
        router=auth_service.routerV1,
        prefix="/api/v1/auth/admin",
        responses=common_private_response,
    )

    admin_dependencies = [
        Depends(admin_authenticator),
    ]

    app.include_router(
        router=admin_service.routerV1,
        prefix="/api/v1/admin",
        dependencies=admin_dependencies,
        responses=common_private_response,
    )

