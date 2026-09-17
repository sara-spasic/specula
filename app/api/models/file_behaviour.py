from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.api.models.ioc_file import File
    from app.api.models.mitre_technique import MITRETechnique
    from app.api.models.sigma_analysis import SigmaAnalysis
    from app.api.models.signature_match import SignatureMatch
    from app.api.models.process_activity import ProcessActivity
    from app.api.models.file_activity import FileActivity
    from app.api.models.service_activity import ServiceActivity
    
from sqlalchemy import Boolean,String,Text,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from  app.api.models.base import Base
from datetime import datetime

class FileBehaviour(Base):
    __tablename__="file_behaviours"
    behaviour_id: Mapped[int]=mapped_column(primary_key=True)

    analysis_date: Mapped[datetime|None]=mapped_column()
    behash: Mapped[str|None]=mapped_column(String)
    sandbox_name: Mapped[str | None] = mapped_column(String)
    verdict_confidence: Mapped[int|None]=mapped_column()
    has_html_report: Mapped[bool|None]=mapped_column(Boolean)
    has_evtx: Mapped[bool|None]=mapped_column(Boolean) 
    has_memdump: Mapped[bool|None]=mapped_column(Boolean) 
    has_pcap:Mapped[bool|None]=mapped_column(Boolean) 
    hosts_file: Mapped[Text|None]=mapped_column(Text)

    file_id: Mapped[int]=mapped_column(
        ForeignKey=("files.file_id")
    )

    file: Mapped["File"]=relationship(
        back_populates="file_behaviours"
    )

    mitre_techniques: Mapped[list["MITRETechnique"]] = relationship(
        back_populates="behaviour"
    )

    sigma_analyses: Mapped[list["SigmaAnalysis"]] = relationship(
        back_populates="behaviour"
    )

    signature_matches: Mapped[list["SignatureMatch"]] = relationship(
        back_populates="behaviour"
    )

    process_activities: Mapped[list["ProcessActivity"]] = relationship(
        back_populates="behaviour"
    )

    file_activities: Mapped[list["FileActivity"]] = relationship(
        back_populates="behaviour"
    )

    service_activities: Mapped[list["ServiceActivity"]] = relationship(
        back_populates="behaviour"
    )