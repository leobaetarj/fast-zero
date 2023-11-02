from dependency_injector import containers, providers

from src.infrastructure.database import Database
from src.infrastructure.repositories.user_repository_orm import (
    UserRepositoryOrm,
)
from src.infrastructure.settings import Settings
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

    db = providers.Singleton(Database, db_url=Settings().DATABASE_URL)

    # pylint: disable=no-member
    user_repository = providers.Factory(
        UserRepositoryOrm, session_factory=db.provided.session
    )

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
