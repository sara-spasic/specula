from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.api.models.abuse_report import AbuseReport
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
    last_reported_at: Mapped[datetime|None]=mapped_column()
    
    
    is_whitelisted: Mapped[bool|None] = mapped_column()
    country_code: Mapped[str|None] = mapped_column()
    country_name: Mapped[str|None] = mapped_column()
    usage_type: Mapped[str|None] = mapped_column()
    isp: Mapped[str|None] = mapped_column()
    domain: Mapped[str|None] = mapped_column()
    is_tor: Mapped[bool|None] = mapped_column()

    reports:Mapped[list["AbuseReport"]]=relationship(
        back_populates="observation"
    )
