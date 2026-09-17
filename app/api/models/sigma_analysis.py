from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.api.models.base import Base

if TYPE_CHECKING:
    from app.api.models.file_behaviour import FileBehaviour


class SigmaAnalysis(Base):
    __tablename__ = "sigma_analyses"

    sigma_analysis_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    behaviour_id: Mapped[int] = mapped_column(
        ForeignKey("file_behaviours.behaviour_id"),
        nullable=False
    )

    rule_title: Mapped[str | None] = mapped_column(String)

    rule_id: Mapped[str | None] = mapped_column(String)

    rule_source:Mapped[str]=mapped_column(String)

    rule_level: Mapped[str]=mapped_column(String)

    severity: Mapped[str | None] = mapped_column(String)

    rule_description: Mapped[str | None] = mapped_column(String)

    rule_author: Mapped[str]=mapped_column(String) 
    
   
    behaviour: Mapped["FileBehaviour"] = relationship(
        back_populates="sigma_analyses"
    )

