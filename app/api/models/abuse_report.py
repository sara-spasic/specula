from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.api.models.abuseipdb_observation import AbuseIPDBObservation

if TYPE_CHECKING:
    from app.api.models.abuse_report_category import AbuseReportCategory
from app.api.models.base import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import Text,String,ForeignKey
from datetime import datetime
class AbuseReport(Base):
    __tablename__ = "abuse_reports"

    report_id: Mapped[int]=mapped_column(primary_key=True)
    reported_at:Mapped[datetime]=mapped_column()
    comment: Mapped[str|None]=mapped_column(Text)
    reporter_id: Mapped[int]=mapped_column()
    reporter_country_code:Mapped[str|None]=mapped_column(String)
    reporter_country_name:Mapped[str|None]=mapped_column(String)

    abuseipdb_observation_id: Mapped[int]=mapped_column(
        ForeignKey("abuseipdb_observations.observation_id")
    )

    observation: Mapped["AbuseIPDBObservation"]=relationship(
        back_populates="reports"
    )

    report_categories: Mapped[list["AbuseReportCategory"]]=relationship(
        back_populates="report"
    )