if TYPE_CHECKING:
    from app.api.models.abuse_report import AbuseReport
from typing import TYPE_CHECKING


from app.api.models.base import Base
from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey

class AbuseReportCategory(Base):
    __tablename__ ="abuse_report_category"

    report_category_id:Mapped[int]=mapped_column(primary_key=True)
    category_id:Mapped[int]=mapped_column()

    report_id:Mapped[int]=mapped_column(
        ForeignKey("abuse_reports.report_id")
    )

    report: Mapped["AbuseReport"]=relationship(
        back_populates="report_categories"
    )