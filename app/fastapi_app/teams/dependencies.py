from typing import Annotated

from fastapi import Depends, Header, HTTPException, Path, status
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import Engineer, Team, db_helper


async def is_team_exists(
        team_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Team:
    stmt = select(Team).options(selectinload(Team.engineers)).where(Team.id == team_id)
    team: Team | None = await session.scalar(stmt)

    if team:
        return team

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Team {team_id} not found.",
    )
