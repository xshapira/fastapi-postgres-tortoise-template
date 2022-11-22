from fastapi import APIRouter, status, Response

from src.core.schemas import Status


router = APIRouter(

)


@router.get(
f"/home",
response_model=Status,
status_code=status.HTTP_200_OK,
tags=['Home'],
description=f"Home endpoint"
)
async def home(response: Response) -> Status:
    return Status(
        message='Hello boils and ghouls'
    )
