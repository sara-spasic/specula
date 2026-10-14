from datetime import datetime, timezone

from sqlalchemy import select

from app.api.models.ioc import IOCType, IOCKind
from app.api.models.ioc_ip import IP
from app.api.models.source import Source
from app.api.models.source_observation import SourceType
from app.api.models.virus_total_observation import VirusTotalObservation


def test_virustotal_observation_is_linked_to_ioc_and_source(db_session):
    now = datetime.now(timezone.utc)

    ioc = IP(
        value="192.0.2.11",
        normalized_value="192.0.2.11",
        type=IOCType.IPV4,
        kind=IOCKind.IP,
        first_seen=now,
        last_seen=now,
    )

    source = Source(name="VirusTotal")

    observation = VirusTotalObservation(
        ioc=ioc,
        source=source,
        fetched_at=now,
        source_type=SourceType.VIRUSTOTAL,
        raw_json={
            "data": {
                "id": "192.0.2.11",
                "type": "ip_address",
            }
        },
    )

    db_session.add(observation)
    db_session.commit()
    observation_id = observation.observation_id

    db_session.expire_all()

    saved_observation = db_session.scalars(
        select(VirusTotalObservation).where(
            VirusTotalObservation.observation_id == observation_id
        )
    ).one()

    assert saved_observation.ioc.value == "192.0.2.11"
    assert saved_observation.source.name == "VirusTotal"
    assert saved_observation.source_type == SourceType.VIRUSTOTAL
    assert saved_observation.raw_json["data"]["type"] == "ip_address"