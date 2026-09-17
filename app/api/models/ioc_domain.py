from sqlalchemy import Boolean,String,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from  app.api.models.ioc import IOC,IOCKind

class Domain(IOC):
    __tablename__="domains"
    __mapper_args__ = {
    "polymorphic_identity": IOCKind.DOMAIN
    }
    ioc_id: Mapped[int] = mapped_column(
            ForeignKey("iocs.ioc_id"),
            primary_key=True
        )

