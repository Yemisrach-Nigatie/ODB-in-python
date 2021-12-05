'''ODBInheritanceST.py'''

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from ODBConnect import Session, engine, Base	

class STBook(Base):
	__tablename__ = "STBOOK"
	book_id = Column(Integer, primary_key=True)
	author_id = Column(Integer)
	title = Column(String(80))
	type = Column(String(80))
	def __init__(self, title):
		self.title = title

	__mapper_args__ = {'polymorphic_on':type, 'polymorphic_identity':'STBook'}

class epubSTBook(STBook):
	__mapper_args__ = {'polymorphic_identity':'epubSTBook'}

class pdfSTBook(STBook):
    	__mapper_args__ = {'polymorphic_identity':'pdfSTBook'}

#——————————————————
Base.metadata.create_all(engine)

session = Session()

book1 = STBook("Fundamentals of Database Systems")
book2 = epubSTBook("Introduction to Probability and Statistics")
book3 = pdfSTBook("Fundamentals of Python: First Programs")

session.add(book1)
session.add(book2)
session.add(book3)

session.commit()
session.close()