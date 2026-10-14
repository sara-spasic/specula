from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.api.models.ioc import IOC
from sqlalchemy import String,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.api.models.base import Base
from datetime import datetime
class RiskAssessment(Base):
    __tablename__="risk_assessments"

    risk_assessment_id: Mapped[int]=mapped_column(primary_key=True)
    risk_score: Mapped[float]=mapped_column()
    risk_level: Mapped[str]=mapped_column(String)
    confidence: Mapped[float]=mapped_column()
    calculated_at: Mapped[datetime]=mapped_column()
    methodology_version: Mapped[str]=mapped_column(String)

    ioc_id: Mapped[int]=mapped_column(
        ForeignKey("iocs.ioc_id")
    )

    ioc: Mapped["IOC"]=relationship(
        back_populates="risk_assessments"
    )

    