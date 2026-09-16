from sqlalchemy import Boolean,String,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from  app.api.models.ioc import IOC

class File(IOC):
    __tablename__="files"

    ioc_id: Mapped[int] = mapped_column(
            ForeignKey("iocs.ioc_id"),
            primary_key=True
        )

    hash_algorithm: Mapped[str] = mapped_column(String)