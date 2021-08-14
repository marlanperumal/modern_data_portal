import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = os.getenv("DB_USER", "postgres")
password = os.getenv("DB_PASSWORD", "postgres")
host = os.getenv("DB_HOST", "db")
db = os.getenv("DB_DB", "postgres")
SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{db}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


from .items import Item  # noqa
from .users import User  # noqa
