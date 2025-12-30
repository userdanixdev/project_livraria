## Conexão com o banco (SQLite + SQLAlchemy)
## database/connection.py

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Banco SQLite
DATABASE_URL = "sqlite:///livraria.db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
