import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.infrastructure.models.base import Base


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    orm_session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield orm_session()
    Base.metadata.drop_all(engine)
