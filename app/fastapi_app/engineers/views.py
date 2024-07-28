from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import db_helper, Engineer

from .dependencies import engineer_to_delete
from .schemas import EngineerCreate, EngineerPatch, EngineerPut
from . import crud

router = APIRouter(tags=["Engineers"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_engineer(
        engineer_data_to_create: EngineerCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_engineer(
        session=session,
        engineer_data=engineer_data_to_create
    )


@router.get("/", status_code=status.HTTP_200_OK)
async def get_engineers(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_engineers(session=session)


@router.delete("/{engineer_id}")
async def delete_engineer(
        engineer: Engineer = Depends(engineer_to_delete),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.delete_engineer(session=session, engineer=engineer)


@router.patch("/{engineer_id}")
async def patch_engineer(
        engineer_data_to_patch: EngineerPatch,
        engineer: Engineer = Depends(engineer_to_delete),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.patch_engineer(session=session, engineer=engineer, engineer_data_to_patch=engineer_data_to_patch)


@router.put("/{engineer_id}")
async def put_engineer(
        engineer_data_to_put: EngineerPut,
        engineer: Engineer = Depends(engineer_to_delete),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.put_engineer(session=session, engineer=engineer, engineer_data_to_put=engineer_data_to_put)
