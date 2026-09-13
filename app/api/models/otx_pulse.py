from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.api.models.otx_observation import OTXObservation

from sqlalchemy import Text,String,Boolean,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from app.api.models.base import Base
from datetime import datetime
class OTXPulse(Base):
    __tablename__="otx_pulses"

    pulse_id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String)
    description:Mapped[str]=mapped_column(Text)
    author_name: Mapped[str]=mapped_column(String)
    tlp:Mapped[str]=mapped_column(String)
    public: Mapped[bool]=mapped_column(Boolean)
    created: Mapped[datetime]=mapped_column()
    modified: Mapped[datetime]=mapped_column()
    adversary: Mapped[str]=mapped_column(String)

    otx_observation_id:Mapped[int]=mapped_column(
        ForeignKey("otx_observations.observation_id")
    )
    observation: Mapped[["OTXObservation"]]=relationship(
        back_populates="pulses"
    )