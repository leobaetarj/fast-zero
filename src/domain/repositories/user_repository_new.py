from abc import ABC, abstractmethod

from src.domain.entities.user import User, UserId


class UserRepository(ABC):
    @abstractmethod
    def add(self, entity: User):
        raise NotImplementedError()

    @abstractmethod
    def remove(self, entity: User):
        raise NotImplementedError()

    @abstractmethod
    def get_by_id(self, user_id: UserId) -> User:
        raise NotImplementedError()

    def __getitem__(self, index) -> User:
        return self.get_by_id(index)
