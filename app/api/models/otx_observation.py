from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.api.models.otx_pulse import OTXPulse

from app.api.models.source_observation import SourceObservation,SourceType
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship

class OTXObservation(SourceObservation):
    __tablename__="otx_observations"
    __mapper_args__ = {
    "polymorphic_identity": SourceType.OTX
    }
    observation_id: Mapped[int]=mapped_column(
        ForeignKey("source_observations.observation_id"),
        primary_key=True
    )

    pulse_count: Mapped[int]=mapped_column()

    pulses: Mapped[list["OTXPulse"]]=relationship(
        back_populates="observation"
    )

