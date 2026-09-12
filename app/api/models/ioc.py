from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.api.models.source_observation import SourceObservation
import enum
from datetime import datetime
from sqlalchemy import Integer,String,Enum,UniqueConstraint
from sqlalchemy.orm import Mapped,mapped_column,relationship



from app.api.models.base import Base

class IOCType(enum.Enum):
    IPV4 = "ipv4"
    IPV6 = "ipv6"
    DOMAIN= "domain"
    URL= "url"
    FILE_HASH= "file_hash"


class IOC(Base):
    __tablename__ = "iocs"
    __table_args__=(
        UniqueConstraint("type","normalized_value"),
    )
    ioc_id: Mapped[int]=mapped_column(Integer,primary_key=True)
    value : Mapped[str]=mapped_column(String,nullable=False)
    normalized_value:Mapped[str]= mapped_column(String,nullable=False)
    type : Mapped[IOCType]=mapped_column(Enum(IOCType),nullable=False)
    first_seen : Mapped[datetime]=mapped_column()
    last_seen :Mapped[datetime]=mapped_column()

    source_observations:Mapped[list["SourceObservation"]]=relationship(
        back_populates="ioc"
    )
