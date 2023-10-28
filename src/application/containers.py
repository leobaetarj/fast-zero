from dependency_injector import containers, providers

from src.infrastructure.repositories.user_repository import UserRepositoryFoo
from src.use_cases.user import (
    CreateUserUseCase,
    DeleteUserUseCase,
    GetUsersUseCase,
    UpdateUserUseCase,
)


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=['.endpoints'])

    # config = providers.Configuration(yaml_files=["config.yml"])
    config = providers.Configuration()

    user_repository = providers.Factory(UserRepositoryFoo)

    create_user_use_case = providers.Factory(
        CreateUserUseCase,
        user_repository=user_repository,
    )

    get_users_use_case = providers.Factory(
        GetUsersUseCase,
        user_repository=user_repository,
    )

    update_user_use_case = providers.Factory(
        UpdateUserUseCase,
        user_repository=user_repository,
    )

    delete_user_use_case = providers.Factory(
        DeleteUserUseCase,
        user_repository=user_repository,
    )
