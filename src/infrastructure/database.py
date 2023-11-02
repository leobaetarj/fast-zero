import logging
from contextlib import AbstractContextManager, contextmanager
from typing import Callable

from sqlalchemy import create_engine, orm
from sqlalchemy.orm import Session, declarative_base

logger = logging.getLogger(__name__)

Base = declarative_base()


class Database:
    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, echo=True)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except Exception:
            logger.exception('Session rollback because of exception')
            session.rollback()
            raise
        finally:
            session.close()


# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session

# from src.infrastructure.settings import Settings

# engine = create_engine(Settings().DATABASE_URL)


# def get_session():
#     with Session(engine) as session:
#         yield session


# class SessionProvider:
#     def __init__(self, session):
#         self.session = session

#     def __call__(self):
#         return next(self.session())
