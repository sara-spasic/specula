from app.api.models.ioc import IOC, IOCType, IOCKind


def test_ioc_creation():
    ioc = IOC(
        value="8.8.8.8",
        normalized_value="8.8.8.8",
        type=IOCType.IPV4,
        kind=IOCKind.IP,
    )

    assert ioc.value == "8.8.8.8"
    assert ioc.normalized_value == "8.8.8.8"
    assert ioc.type == IOCType.IPV4
    assert ioc.kind == IOCKind.IP


    