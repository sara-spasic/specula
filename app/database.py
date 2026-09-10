import os
import sqlalchemy as db

DATABASE_URL = os.getenv("DATABASE_URL")


engine = db.create_engine(DATABASE_URL)

