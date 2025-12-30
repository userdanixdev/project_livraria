## Modelos ORM (entidades):
# database/models.py

from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .connection import Base

# Entity: Publisher

class Publisher(Base):
    __tablename__ = "publisher"

    id_publisher = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cnpj = Column(String, unique=True, nullable=False)
    contact = Column(String)

    books = relationship("Book", back_populates="publisher")

# Category

class Category(Base):
    __tablename__='category'

    id_category = Column(Integer, primary_key=True, index=True)
    name_category = Column(String, nullable=False)
    description = Column(String)

    books = relationship('Book', back_populates = 'category')

# Entity: Book

class Book(Base):
    __tablename__ = 'book'
    # Colunas e atributos:
    isbn = Column(String,primary_key=True)
    title = Column(String, nullable=False)
    year_publication = Column(Integer)
    price = Column(Float)
    edition = Column(String)
    stock = Column(Integer)
    # Chaves estrangeiras:
    id_publisher = Column(Integer, ForeignKey('publisher.id_publisher'))
    id_category = Column(Integer, ForeignKey('category.id_category'))
    # Relações:
    publisher = relationship('Publisher', back_populates = 'books')
    category = relationship('Category', back_populates = 'books')
    authors = relationship('BookAuthor', back_populates = 'book')
    items_sale = relationship('ItemSale', back_populates = 'book')

# Entity: Author

class Author(Base):
    __tablename__ = 'author'
    # Colunas e atributos:    
    id_author = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    nationality = Column(String)
    # Relações:
    books = relationship("BookAuthor", back_populates='author')

# Entity: BookAuthor (entidade associativa)    

class BookAuthor(Base):
    __tablename__ = 'book_author'
    # Chave Composta:
    isbn = Column(String, ForeignKey('book.isbn'), primary_key=True)
    id_author = Column(Integer, ForeignKey('author.id_author'),primary_key=True)
    # Relações:
    book = relationship('Book',back_populates='authors')
    author = relationship('Author',back_populates='books')

# Entity: employee

class Employee(Base):
    __tablename__= 'employee'

    id_employee = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)    
    # Relações:
    sales = relationship("Sale", back_populates='employee')

# Entity: Client

class Client(Base):
    __tablename__ = 'client'

    id_client = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    email = Column(String)
    phone = Column(String)
    # Relações:
    sales =  relationship("Sale",back_populates='client')

# Entity: Sale

class Sale(Base):
    __tablename__ = 'sale'
    # Colunas e atributos:
    id_sale = Column(Integer, primary_key=True, index= True)
    date_sale = Column(Date)
    valor_total = Column(Float)
    payment_method = Column(String)

    # Chaves:
    id_client = Column(Integer, ForeignKey('client.id_client'))
    id_employee = Column(Integer,ForeignKey('employee.id_employee'))
    # Relações:
    client = relationship("Client", back_populates='sales')
    employee = relationship("Employee", back_populates='sales')
    items=relationship("ItemSale", back_populates='sale')

# ItemSale (entidade associativa)

class ItemSale(Base):
    __tablename__ =  "item_sale"    

    id_sale = Column(Integer, ForeignKey("sale.id_sale"), primary_key=True)
    isbn = Column(String, ForeignKey("book.isbn"), primary_key=True)
    quantity = Column(Integer, nullable=False)
    price_unit = Column(Float, nullable=False)

    sale = relationship("Sale", back_populates="items")
    book = relationship("Book", back_populates="items_sale")


    




