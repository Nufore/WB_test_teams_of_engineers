from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import Team, db_helper

from . import crud
from .dependencies import is_team_exists
from .schemas import TeamCreate

router = APIRouter(tags=["Teams"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_team(
        team_data_to_create: TeamCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_team(session=session, team_data=team_data_to_create)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_teams(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_teams(session=session)


@router.get("/{team_id}", status_code=status.HTTP_200_OK)
async def get_team(
        team: Team = Depends(is_team_exists)
):
    return team.to_json()


@router.delete("/{team_id}")
async def delete_team(
        team: Team = Depends(is_team_exists),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.delete_team(session=session, team=team)


@router.put("/{team_id}")
async def put_team(
        team_data_to_put: TeamCreate,
        team: Team = Depends(is_team_exists),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.put_team(session=session, team=team, team_data_to_put=team_data_to_put)
