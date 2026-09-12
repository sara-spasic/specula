from app.api.models.source_observation import SourceObservation
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from datetime import datetime

class AbuseIPDBObservation(SourceObservation):
    __tablename__="abuseipdb_observations"

    observation_id: Mapped[int] = mapped_column(
            ForeignKey("source_observations.observation_id"),
            primary_key=True
        )
    abuse_confidence_score: Mapped[int]=mapped_column()
    total_reports: Mapped[int]=mapped_column()
    num_distinct_users: Mapped[int]=mapped_column()
    last_reported_at: Mapped[datetime]=mapped_column()
    