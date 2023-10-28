from src.domain.entities.user import User, UserId
from src.domain.repositories.user_repository import UserRepository

users_storage = []


class UserRepositoryFoo(UserRepository):
    def _find_user_index_by_id(self, users, user_id):
        for index, user in enumerate(users):
            if str(user.id) == str(user_id):
                return index
        return None

    async def create(self, user: User) -> bool:
        users_storage.append(user)
        return True

    def get_all(self) -> list[User]:
        return users_storage

    def update(self, user: User) -> bool:
        index = self._find_user_index_by_id(users_storage, user.id)

        if index is not None:
            users_storage[index] = user
            return True

        return False

    def delete(self, user_id: UserId) -> bool:
        index = self._find_user_index_by_id(users_storage, user_id)

        if index is not None:
            del users_storage[index]
            return True

        return False
