from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.api.models.source_observation import SourceObservation
from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.api.models.base import Base
class Source(Base):
    __tablename__="source"
    source_id: Mapped[int]=mapped_column(primary_key=True)

    name:Mapped[str]=mapped_column(String)

    observations: Mapped[list["SourceObservation"]]= relationship(
        back_populates="source"
    )