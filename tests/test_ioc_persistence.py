from datetime import datetime, timezone

from sqlalchemy import select

from app.api.models.ioc import IOC, IOCType, IOCKind
from app.api.models.ioc_ip import IP


def test_ip_ioc_can_be_saved_and_retrieved(db_session):
    now = datetime.now(timezone.utc)

    ioc = IP(
        value="192.0.2.10",
        normalized_value="192.0.2.10",
        type=IOCType.IPV4,
        kind=IOCKind.IP,
        first_seen=now,
        last_seen=now,
    )

    db_session.add(ioc)
    db_session.commit()
    ioc_id = ioc.ioc_id

    db_session.expire_all()

    saved_ioc = db_session.scalars(
        select(IOC).where(IOC.ioc_id == ioc_id)
    ).one()

    assert isinstance(saved_ioc, IP)
    assert saved_ioc.value == "192.0.2.10"
    assert saved_ioc.normalized_value == "192.0.2.10"
    assert saved_ioc.type == IOCType.IPV4
    assert saved_ioc.kind == IOCKind.IP