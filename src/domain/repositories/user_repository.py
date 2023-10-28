from abc import ABC, abstractmethod

from src.domain.entities.user import User, UserId


class UserRepository(ABC):
    @abstractmethod
    async def create(self, user: User) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abstractmethod
    def update(self, user: User) -> bool:
        pass

    @abstractmethod
    def delete(self, user_id: UserId) -> bool:
        pass
