'''ODBQueries.py'''

from ODBIntension import Book, Publisher
from ODBConnect import Session, engine, Base	
	
# 1 - generate database schema
Base.metadata.create_all(engine)

# 2 - Open a new session
session = Session()

# 3 - retrieve stored books and their total number
list_of_books = session.query(Book).all()
number_of_books = session.query(Book).count()
 
# 4 - retrieve books starts with letter 'F'
special_books = session.query(Book).filter(Book.Title.ilike('F%')).all()

# 5 - Display results
print('********** List of Books **********')
for book in list_of_books:
	print(book.Title)
print('Currently there are ' + str(number_of_books) + ' books in the database and ' + str(len(special_books)) + ' of them start with letter \'F\'.')
print('********** ************* **********')


# 6 - commit and close session
session.commit()
session.close()
