from unittest import mock
from uuid import UUID

from src.application.app import app
from src.domain.entities.user import User, UserId
from src.domain.repositories.user_repository import UserRepository


def test_root_must_returns_200_and_expected_string(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Home sweet home!'}


def test_post_users(client):
    repository_mock = mock.Mock(spec=UserRepository)
    repository_mock.create.return_value = True

    with app.container.user_repository.override(repository_mock):
        response = client.post(
            '/users/',
            json={
                'username': 'alice',
                'email': 'alice@example.com',
                'password': 'secret',
            },
        )

    assert response.status_code == 201

    response_body = response.json()
    assert 'user' in response_body
    assert 'username' in response_body['user']
    assert 'email' in response_body['user']

    assert UUID(response_body['user']['id'])
    assert response_body['user']['username'] == 'alice'
    assert response_body['user']['email'] == 'alice@example.com'
    assert 'password' not in response_body['user']


def test_get_users(client):
    repository_mock = mock.Mock(spec=UserRepository)
    repository_mock.get_all.return_value = [
        User(
            id=UserId(),
            username='alice',
            email='alice@example.com',
            password='secret',
        ),
        User(
            id=UserId(),
            username='leo',
            email='leo@example.com',
            password='secret',
        ),
    ]

    with app.container.user_repository.override(repository_mock):
        response = client.get('/users/')

    assert response.status_code == 200

    response_body = response.json()

    assert 'users' in response_body
    assert isinstance(response_body['users'], list)

    user1 = response_body['users'][0]
    assert UUID(user1['id'])
    assert user1['username'] == 'alice'
    assert user1['email'] == 'alice@example.com'
    assert 'password' not in user1

    user2 = response_body['users'][1]
    assert UUID(user2['id'])
    assert user2['username'] == 'leo'
    assert user2['email'] == 'leo@example.com'
    assert 'password' not in user2


def test_update_user(client):
    repository_mock = mock.Mock(spec=UserRepository)
    repository_mock.update.return_value = True

    user_id = 'a09c23e6-615e-4490-b17d-4c92c85b9243'

    with app.container.user_repository.override(repository_mock):
        response = client.put(
            f'/users/{user_id}',
            json={
                'username': 'alice',
                'email': 'alice@example.com',
                'password': 'secret',
            },
        )

    assert response.status_code == 200

    response_body = response.json()
    assert 'user' in response_body
    assert 'username' in response_body['user']
    assert 'email' in response_body['user']

    assert response_body['user']['id'] == user_id
    assert response_body['user']['username'] == 'alice'
    assert response_body['user']['email'] == 'alice@example.com'
    assert 'password' not in response_body['user']


def test_delete_user(client):
    repository_mock = mock.Mock(spec=UserRepository)
    repository_mock.delete.return_value = True

    user_id = 'a09c23e6-615e-4490-b17d-4c92c85b9243'

    with app.container.user_repository.override(repository_mock):
        response = client.delete(f'/users/{user_id}')

    assert response.status_code == 200
