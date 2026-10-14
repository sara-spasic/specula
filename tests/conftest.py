
import os

from requests import Session

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.engine import make_url


@pytest.fixture(scope="session")
def test_engine():
    database_url = os.getenv("TEST_DATABASE_URL")

    if not database_url:
        pytest.fail("TEST_DATABASE_URL is not configured.")

    url = make_url(database_url)

    if url.database != "specula_test":
        pytest.fail(
            f"Tests must not use the database: {url.database}"
        )

    engine = create_engine(database_url)

    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT current_database()")
            ).scalar_one()

            if result != "specula_test":
                pytest.fail(
                    f"The wrong database is connected: {result}"
                )

        yield engine
    finally:
        engine.dispose()


@pytest.fixture
def db_session(test_engine):
    connection = test_engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()
        connection.close()