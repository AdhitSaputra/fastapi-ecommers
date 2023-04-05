from fastapi import APIRouter, Depends
from fastapi_pagination import Params

from schemas.response_schema import IGetResponsePaginated

router = APIRouter()

@router.get("/list"):
async def read_user_list(
    params: Params = Depends(),
) -> IGetResponsePaginated[IUserReadWithoutGroups]:
