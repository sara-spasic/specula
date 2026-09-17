from typing import TYPE_CHECKING

if TYPE_CHECKING:
        from app.api.models.file_behaviour import FileBehaviour
from sqlalchemy import Boolean,String,Text,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from  app.api.models.base import Base

class MITREtechnique(Base):
        __tablename__ = "mitre_techniques"

        technique_id: Mapped[int]=mapped_column(primary_key=True)

        mitre_id: Mapped[str]=mapped_column(String) 
        severity: Mapped[str]=mapped_column(String) 
        signature_description: Mapped[str | None]=mapped_column(Text)

        file_behaviour_id: Mapped[int]=mapped_column(
                ForeignKey("file_behaviours.behaviour_id")
        )

        behaviour: Mapped["FileBehaviour"]=relationship(
                back_populates="mitre_techniques"
        )