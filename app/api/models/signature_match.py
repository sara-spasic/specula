from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String,Text,JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.api.models.base import Base

if TYPE_CHECKING:
    from app.api.models.file_behaviour import FileBehaviour


class SignatureMatch(Base):
    __tablename__ = "signature_matches"

    signature_match_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    behaviour_id: Mapped[int] = mapped_column(
        ForeignKey("file_behaviours.behaviour_id"),
        nullable=False
    )

    format: Mapped[str] =mapped_column(String) 
    authors:Mapped[dict|None]=mapped_column(JSON) 

    signature_type: Mapped[str | None] = mapped_column(String)

    rule_src: Mapped[str]=mapped_column(String) 

    signature_name: Mapped[str | None] = mapped_column(
        String
    )

    description: Mapped[str | None] = mapped_column(Text)

    behaviour: Mapped["FileBehaviour"] = relationship(
        back_populates="signature_matches"
    )
   
