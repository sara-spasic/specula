from app.api.models.ioc import IOC, IOCType, IOCKind

from app.api.models.ioc_ip import IP
from app.api.models.ioc_domain import Domain
from app.api.models.ioc_url import URL
from app.api.models.ioc_file import File

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


def test_ioc_type_values():
    assert IOCType.IPV4.value == "ipv4"
    assert IOCType.IPV6.value == "ipv6"
    assert IOCType.DOMAIN.value == "domain"
    assert IOCType.URL.value == "url"
    assert IOCType.FILE_HASH.value == "file_hash"


def test_ioc_kind_values():
    assert IOCKind.IP.value == "ip"
    assert IOCKind.DOMAIN.value == "domain"
    assert IOCKind.URL.value == "url"
    assert IOCKind.FILE.value == "file"


def test_ioc_subclasses_have_correct_mapper_identity():
    assert IP.__mapper__.polymorphic_identity == IOCKind.IP
    assert Domain.__mapper__.polymorphic_identity == IOCKind.DOMAIN
    assert URL.__mapper__.polymorphic_identity == IOCKind.URL
    assert File.__mapper__.polymorphic_identity == IOCKind.FILE

