from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.api.models.file_behaviour import FileBehaviour
from sqlalchemy import Boolean,String,ForeignKey
from sqlalchemy.orm import Mapped,mapped_column,relationship
from  app.api.models.ioc import IOC

class File(IOC):
    __tablename__="files"

    ioc_id: Mapped[int] = mapped_column(
            ForeignKey("iocs.ioc_id"),
            primary_key=True
        )

    hash_algorithm: Mapped[str|None] = mapped_column(String)

    file_behaviours: Mapped[list["FileBehaviour"]]=relationship(
        back_populates="file"
    )