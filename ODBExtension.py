'''ODBExtension.py'''

from ODBIntension import Book, Publisher
from ODBConnect import Session, engine, Base	
	
# 1 - generate database schema
Base.metadata.create_all(engine)

# 2 - create a new session
session = Session()

# 3 - create books
book1 = Book("Fundamentals of Database Systems")
book2 = Book("Introduction to Probability and Statistics")
book3 = Book("Fundamentals of Python: First Programs")

# 4 - create publishers
Pub1 = Publisher("Pearson")
Pub2 = Publisher("Cengage")


# 5 - add publishers to books
book1.publishers = [Pub1]
book2.publishers = [Pub2]
book3.publishers = [Pub2]


# 6 - persists data
session.add(book1)
session.add(book2)
session.add(book3)

session.add(Pub1)
session.add(Pub2)


# 7 - commit and close session
session.commit()
session.close()
