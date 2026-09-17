from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.api.models.base import Base

if TYPE_CHECKING:
    from app.api.models.file_behaviour import FileBehaviour
import enum
class FileActivityType(enum.Enum):
    OPENED="opened"
    WRITTEN ="written"
    DELETED="deleted"
    ATTRIBUTE_CHANGED="attribute_changed"

class FileActivity(Base):
    __tablename__ = "file_activities"

    file_activity_id: Mapped[int] = mapped_column(primary_key=True)

    behaviour_id: Mapped[int] = mapped_column(
        ForeignKey("file_behaviours.behaviour_id"),
        nullable=False
    )

    file_name: Mapped[str | None] = mapped_column(String)

    file_path: Mapped[str | None] = mapped_column(
        String
    )

  
    activity_type: Mapped[FileActivityType]=mapped_column(Enum(FileActivityType))

    action: Mapped[str | None] = mapped_column(
        String
    )

    behaviour: Mapped["FileBehaviour"] = relationship(
        back_populates="file_activities"
    )