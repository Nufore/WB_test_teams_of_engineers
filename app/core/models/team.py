from typing import TYPE_CHECKING

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .engineer import Engineer


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)

    engineers: Mapped[list["Engineer"]] = relationship(
        back_populates="team",
        cascade="save-update"
    )

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "engineers": [engineer.to_json() for engineer in self.engineers]
        }
