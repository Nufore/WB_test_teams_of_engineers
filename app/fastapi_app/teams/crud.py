from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from fastapi import HTTPException, status

from app.core.models import Engineer, Team

from .schemas import TeamCreate


async def create_team(
        session: AsyncSession,
        team_data: TeamCreate
):
    new_team = Team(name=team_data.name)
    session.add(new_team)
    await session.commit()
    return {
        "result": True
    }


async def get_teams(session: AsyncSession):
    stmt = (
        select(Team).options(selectinload(Team.engineers)).order_by(Team.id)
    )

    res = await session.scalars(stmt)
    teams = res.all()

    return {
        "teams": [team.to_json() for team in teams]
    }


async def delete_team(
        session: AsyncSession,
        team: Team
):
    await session.delete(team)
    await session.commit()
    return {
        "result": True
    }


async def put_team(
        session: AsyncSession,
        team: Team,
        team_data_to_put: TeamCreate
):
    team.name = team_data_to_put.name
    session.add(team)
    await session.commit()
    return {
        "result": True
    }