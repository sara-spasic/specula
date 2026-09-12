from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.api.models.virus_total_observation import VirusTotalObservation
from app.api.models.base import Base
from sqlalchemy import String,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from datetime import datetime

class VirusTotalAnalysisResult(Base):
    __tablename__ = "virus_total_analysis_results"

    result_id: Mapped[int]=mapped_column(primary_key=True)
    observation_id: Mapped[int] = mapped_column(
        ForeignKey("virus_total_observations.observation_id")
    )
    observation: Mapped["VirusTotalObservation"] = relationship(
        back_populates="analysis_results"
    )
    engine_name: Mapped[str]=mapped_column(String)
    engine_version: Mapped[str]=mapped_column(String)
    category:Mapped[str]=mapped_column(String)
    method:Mapped[str]=mapped_column(String)
    result: Mapped[str]=mapped_column(String)



