from src.domain.entities.user import User, UserId
from src.infrastructure.models.user import UserModel


def user_entity_to_model(entity: User):
    return UserModel(
        id=str(entity.id),
        username=entity.username,
        password=entity.password,
        email=entity.email,
    )


def user_model_to_entity(model: UserModel):
    return User(
        id=UserId(model.id),
        username=model.username,
        password=model.password,
        email=model.email,
    )
