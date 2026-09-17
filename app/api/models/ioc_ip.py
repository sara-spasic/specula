from sqlalchemy import Boolean,String,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from  app.api.models.ioc import IOC,IOCKind

class IP(IOC):
    __tablename__="ips"

    __mapper_args__ = {
    "polymorphic_identity": IOCKind.IP
    }
    ioc_id: Mapped[int] = mapped_column(
            ForeignKey("iocs.ioc_id"),
            primary_key=True
        )

   