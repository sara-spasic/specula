from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.api.models.otx_pulse import OTXPulse

from app.api.models.source_observation import SourceObservation
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship

class OTXObservation(SourceObservation):
    ___tablename___="otx_observations"
    observation_id: Mapped[int]=mapped_column(
        ForeignKey("source_observations.observation_id"),
        primary_key=True
    )

    pulse_count: Mapped[int]=mapped_column()

    pulses: Mapped[list["OTXPulse"]]=relationship(
        back_populates="observation"
    )

