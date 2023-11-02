import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.application.app import app
from src.infrastructure.models.base import Base


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    orm_session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield orm_session()
    Base.metadata.drop_all(engine)
