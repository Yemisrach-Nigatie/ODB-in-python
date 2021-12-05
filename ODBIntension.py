
''' ODBIntension.py '''

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from ODBConnect import Session, engine, Base	



book_publisher = Table("book_publisher", Base.metadata,
	Column("Book_id", Integer, ForeignKey("BOOK.Book_id")),
	Column("Publisher_name", String(80), ForeignKey("PUBLISHER.Publisher_name")),)

class Book(Base):
	__tablename__ = "BOOK"
	Book_id = Column(Integer, primary_key=True)
	Title = Column(String(80))
	Publisher_name = Column(String(80))
	publishers = relationship("Publisher", secondary=book_publisher, back_populates="books")
	def __init__(self, Title):
		self.Title = Title


class Publisher(Base):
	__tablename__ = "PUBLISHER"
	Publisher_name = Column(String(80), primary_key=True)
	Address = Column(String(80))
	Phone = Column(String(80))
	books = relationship("Book", secondary=book_publisher, back_populates="publishers")
	def __init__(self, Publisher_name):
		self.Publisher_name = Publisher_name