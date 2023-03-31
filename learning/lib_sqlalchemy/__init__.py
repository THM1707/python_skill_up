from sqlalchemy import create_engine

from .configs import Config

c = Config()

engine = create_engine(
    f"{c.DB_ENGINE}://{c.DB_USER}:{c.DB_PASSWORD}@{c.DB_HOST}:{c.DB_PORT or 3306}/{c.DB_NAME}",
    echo=True,
    future=True
)
