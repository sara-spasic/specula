from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.api.models.virus_total_analysis_res import VirusTotalAnalysisResult
from app.api.models.source_observation import SourceObservation
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from datetime import datetime

class VirusTotalObservation(SourceObservation):
    __tablename__ = "virus_total_observations"
    observation_id: Mapped[int] = mapped_column(
        ForeignKey("source_observations.observation_id"),
        primary_key=True
    )
    first_submission_date: Mapped[datetime] = mapped_column()
    last_submission_date: Mapped[datetime]=mapped_column()
    last_analysis_date:Mapped[datetime]=mapped_column()
    last_modification_date:Mapped[datetime]=mapped_column()
    times_submitted: Mapped[int]=mapped_column()
    reputation:Mapped[int]=mapped_column()
    malicious_count:Mapped[int]=mapped_column()
    suspicious_count:Mapped[int]=mapped_column()
    harmless_count:Mapped[int]=mapped_column()
    undetected_count:Mapped[int]=mapped_column()
    timeout_count:Mapped[int]=mapped_column()
    votes_harmless:Mapped[int]=mapped_column()
    votes_malicious:Mapped[int]=mapped_column()
    unique_sources:Mapped[int]=mapped_column()

    analysis_results: Mapped[list["VirusTotalAnalysisResult"]] = relationship(
        back_populates="observation"
    )





