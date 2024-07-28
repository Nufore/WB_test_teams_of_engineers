from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from app.core.models import Engineer, Team

from .schemas import EngineerCreate, EngineerPatch, EngineerPut
from .dependencies import check_team


async def create_engineer(
        session: AsyncSession,
        engineer_data: EngineerCreate
):
    new_engineer = Engineer(
        first_name=engineer_data.first_name,
        last_name=engineer_data.last_name
    )
    session.add(new_engineer)
    await session.commit()
    return {
        "result": True
    }


async def get_engineers(
        session: AsyncSession
):
    stmt = (
        select(Engineer).order_by(-Engineer.id)
    )

    res = await session.scalars(stmt)
    engineers = res.all()

    return {
        "engineers": [engineer.to_json() for engineer in engineers]
    }


async def delete_engineer(
        session: AsyncSession,
        engineer: Engineer
):
    await session.delete(engineer)
    await session.commit()
    return {
        "result": True
    }


async def patch_engineer(
        session: AsyncSession,
        engineer: Engineer,
        engineer_data_to_patch: EngineerPatch
):
    data = engineer_data_to_patch.dict(exclude_unset=True)

    if "team_id" in data:
        await check_team(session=session, team_id=data["team_id"])

    for attr in data:
        if hasattr(engineer, attr):
            setattr(engineer, attr, data[attr])
    session.add(engineer)
    await session.commit()
    return {
        "result": True
    }


async def put_engineer(
        session: AsyncSession,
        engineer: Engineer,
        engineer_data_to_put: EngineerPut
):
    await check_team(session=session, team_id=engineer_data_to_put.team_id)

    engineer.first_name = engineer_data_to_put.first_name
    engineer.last_name = engineer_data_to_put.last_name
    engineer.team_id = engineer_data_to_put.team_id

    session.add(engineer)
    await session.commit()
    return {
        "result": True
    }
