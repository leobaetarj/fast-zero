from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException

from src.application.schemas import (
    CreateUserRequest,
    CreateUserResponse,
    DeleteUserResponse,
    GetUsersResponse,
    UpdateUserRequest,
    UpdateUserResponse,
    UserPayload,
)
from src.use_cases.user import (
    CreateUserUseCase,
    DeleteUserUseCase,
    GetUsersUseCase,
    UpdateUserUseCase,
)

from .containers import Container

router = APIRouter()


@router.get('/')
def home():
    return {'message': 'Home sweet home!'}


@router.post('/users/', status_code=201, response_model=CreateUserResponse)
@inject
async def create_user(
    user_request: CreateUserRequest,
    use_case: CreateUserUseCase = Depends(
        Provide[Container.create_user_use_case]
    ),
):
    user = use_case.execute(user_request)

    user_payload = UserPayload(
        id=str(user.id), username=user.username, email=user.email
    )

    return CreateUserResponse(user=user_payload)


@router.get('/users/', response_model=GetUsersResponse)
@inject
def get_users(
    use_case: GetUsersUseCase = Depends(Provide[Container.get_users_use_case]),
):
    users = use_case.execute()

    users_payload = map(
        lambda user: UserPayload(
            id=str(user.id), username=user.username, email=user.email
        ),
        users,
    )

    return GetUsersResponse(users=users_payload)


@router.put('/users/{user_id}', response_model=UpdateUserResponse)
@inject
def update_user(
    user_id: str,
    user_request: UpdateUserRequest,
    use_case: UpdateUserUseCase = Depends(
        Provide[Container.update_user_use_case]
    ),
):
    try:
        user = use_case.execute(user_id, user_request)
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error)) from error

    user_payload = UserPayload(
        id=str(user.id), username=user.username, email=user.email
    )

    return UpdateUserResponse(user=user_payload)


@router.delete('/users/{user_id}', response_model=DeleteUserResponse)
@inject
def delete_user(
    user_id: str,
    use_case: DeleteUserUseCase = Depends(
        Provide[Container.delete_user_use_case]
    ),
):
    try:
        use_case.execute(user_id)
    except Exception as error:
        raise HTTPException(status_code=404, detail=str(error)) from error

    return DeleteUserResponse(detail=f'User {user_id} deleted')
