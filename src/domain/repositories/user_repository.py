from abc import ABC, abstractmethod

from src.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> bool:
        pass

    @abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abstractmethod
    def update(self, user: User) -> bool:
        pass

    @abstractmethod
    def delete(self, user: User) -> bool:
        pass
