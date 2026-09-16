from sqlalchemy import Boolean,String,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from  app.api.models.ioc import IOC

class IP(IOC):
    __tablename__="ips"

    ioc_id: Mapped[int] = mapped_column(
            ForeignKey("iocs.ioc_id"),
            primary_key=True
        )

    ip_version: Mapped[int] = mapped_column()