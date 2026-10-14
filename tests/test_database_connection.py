from sqlalchemy import text
from conftest import test_engine


def test_connection_uses_test_database(test_engine):
    with test_engine.connect() as connection:
        database_name = connection.execute(
            text("SELECT current_database()")
        ).scalar_one()

    assert database_name == "specula_test"