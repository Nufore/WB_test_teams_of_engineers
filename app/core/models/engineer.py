from typing import TYPE_CHECKING

from sqlalchemy import Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .team import Team


class Engineer(Base):
    __tablename__ = "engineers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(Text, nullable=False)
    last_name: Mapped[str] = mapped_column(Text, nullable=False)

    team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id", ondelete="SET NULL"),
        nullable=True
    )
    team: Mapped["Team"] = relationship("Team", back_populates="engineers")

    def to_json(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
