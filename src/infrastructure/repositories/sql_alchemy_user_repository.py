from sqlalchemy.orm import Session

from src.domain.entities.user import User, UserId
from src.domain.repositories.user_repository_new import UserRepository
from src.infrastructure.data_mappers.user import (
    user_entity_to_model,
    user_model_to_entity,
)
from src.infrastructure.models.user import UserModel

REMOVED = object()

# TODO: work with __init__.py files correctly
# Example: src/infrastructure/data_mappers/__init__.py


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session, identity_map=None):
        self.session = session
        self._identity_map = identity_map or {}

    def add(self, entity: User):
        self._identity_map[str(entity.id)] = entity
        model = user_entity_to_model(entity)
        self.session.add(model)

    def remove(self, entity: User):
        self._check_not_removed(entity)

        self._identity_map[str(entity.id)] = REMOVED
        model = self.session.get(UserModel, str(entity.id))
        self.session.delete(model)

    def get_by_id(self, user_id: UserId):
        if str(user_id) in self._identity_map:
            return self._identity_map[str(user_id)]

        model = self.session.get(UserModel, str(user_id))

        if model is None:
            return None

        entity = user_model_to_entity(model)

        self._check_not_removed(entity)

        self._identity_map[str(entity.id)] = entity

        return entity

    def _check_not_removed(self, entity):
        assert (
            self._identity_map.get(str(entity.id), None) is not REMOVED
        ), f'Entity {entity.id} already removed'
