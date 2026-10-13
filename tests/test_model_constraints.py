from app.api.models.base import Base
from app.api.models.ioc import IOC


def test_ioc_has_unique_type_and_normalized_value_constraint():
    constraints = IOC.__table__.constraints

    matching_constraints = [
        constraint
        for constraint in constraints
        if constraint.__class__.__name__ == "UniqueConstraint"
        and {column.name for column in constraint.columns}
        == {"type", "normalized_value"}
    ]

    assert len(matching_constraints) == 1


def test_ioc_required_columns_are_not_nullable():
    table = Base.metadata.tables["iocs"]

    required_columns = [
        "value",
        "normalized_value",
        "type",
        "kind",
    ]

    for column_name in required_columns:
        assert table.columns[column_name].nullable is False

