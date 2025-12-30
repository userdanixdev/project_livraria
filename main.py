# Depois de atribuir as classes. Eis a criação das tabelas no banco de dados:

from database.connection import engine, Base
from database import models

def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()


# Isso criará o arquivo livraria.db com todas as tabelas.