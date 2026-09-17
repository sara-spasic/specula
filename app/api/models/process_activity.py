from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text,Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum
from app.api.models.base import Base

if TYPE_CHECKING:
    from app.api.models.file_behaviour import FileBehaviour

class ProcessActivityType(enum.Enum):
    TERMINATED="terminated" 
    KILLED ="killed"
    INJECTED="injected"


class ProcessActivity(Base):
    __tablename__ = "process_activities"

    process_activity_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    behaviour_id: Mapped[int] = mapped_column(
        ForeignKey("file_behaviours.behaviour_id"),
        nullable=False
    )

    process_name: Mapped[str | None] = mapped_column(
        String
    )

    process_id: Mapped[int | None] = mapped_column()

    parent_process_id: Mapped[int | None] = mapped_column()

    activity_type: Mapped[ProcessActivityType]=mapped_column(Enum(ProcessActivityType))
    command_line: Mapped[str | None] = mapped_column(Text)

    path: Mapped[str | None] = mapped_column(String)

    behaviour: Mapped["FileBehaviour"] = relationship(
        back_populates="process_activities"
    )

