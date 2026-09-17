from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.api.models.source import Source
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.api.models.ioc import IOC
from sqlalchemy import JSON,ForeignKey,Enum
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.api.models.base import Base
from datetime import datetime
import enum

class SourceType(enum.Enum):
    VIRUSTOTAL = "virustotal"
    ABUSEIPDB = "abuseipdb"
    OTX = "otx"
class SourceObservation(Base):
    __tablename__ ="source_observations"
    observation_id: Mapped[int] = mapped_column(primary_key=True)
    source_id : Mapped[int]=mapped_column(
        ForeignKey("source.source_id")
    )
    ioc_id:Mapped[int]=mapped_column(
        ForeignKey("iocs.ioc_id")
    )
    fetched_at: Mapped[datetime]=mapped_column()
    raw_json: Mapped[dict] = mapped_column(JSON,nullable=False)
    source: Mapped["Source"]=relationship(
        back_populates="observations"
    )
    ioc:Mapped["IOC"]=relationship(
        back_populates="source_observations"
    )

    source_type: Mapped[SourceType] = mapped_column(Enum(SourceType),nullable=False)

    __mapper_args__ = {
    "polymorphic_on": source_type
    }