from sqlalchemy.orm import configure_mappers

import app.api.models


def test_all_model_mappers_configure():
    configure_mappers()
