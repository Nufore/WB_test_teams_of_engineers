from typing import Annotated

from fastapi import Depends, Header, HTTPException, Path, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import Engineer, Team, db_helper


async def engineer_to_delete(
        engineer_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Engineer:
    stmt = select(Engineer).where(Engineer.id == engineer_id)
    engineer: Engineer | None = await session.scalar(stmt)

    if engineer:
        return engineer

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Engineer {engineer_id} not found.",
    )


async def check_team(session: AsyncSession, team_id: int):
    stmt = select(Team).where(Team.id == team_id)
    team: Team | None = await session.scalar(stmt)
    if not team:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Team {team_id} not found.",
        )
