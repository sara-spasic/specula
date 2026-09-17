
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String,Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum
from app.api.models.base import Base

if TYPE_CHECKING:
    from app.api.models.file_behaviour import FileBehaviour

class ServiceActivityType(enum.Enum):
        OPENED="opened"
        CREATED="created"
        STARTED="started"
        STOPPED="stopped"
        DELETED="deleted"
        BOUND="bound"

class ServiceActivity(Base):
    __tablename__ = "service_activities"

    service_activity_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    behaviour_id: Mapped[int] = mapped_column(
        ForeignKey("file_behaviours.behaviour_id"),
        nullable=False
    )

    service_name: Mapped[str | None] = mapped_column(
        String
    )

    action: Mapped[str | None] = mapped_column(
        String
    )

    activity_type: Mapped[ServiceActivityType]=mapped_column(Enum(ServiceActivityType))

    behaviour: Mapped["FileBehaviour"] = relationship(
        back_populates="service_activities"
    )