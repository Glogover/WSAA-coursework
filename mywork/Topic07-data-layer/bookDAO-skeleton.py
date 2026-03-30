# Book DAO skeleton code
# This is a demonstration of the type of function a data layer might have
# Author: Marcin Kaminski

class BookDAO: # Data Access Object for books, class that will handle all interactions with the data source (e.g., database)
    # get all books
    def get_all(self):
        return [{"id": 1, "title": "blah", "author": "someone", "price": 999}]
    # find by id
    def find_by_id(self, id):
        return {"id": id, "title": "blah", "author": "someone", "price": 999}
    # create a book
    def create(self, book):
        return {"id":1, "title": "blah", "author": "someone", "price": 999}
    # update a book
    def update(self, id, book):
        return {"id": id, "title": "blah", "author": "someone", "price": 999}
    # delete a book
    def delete(self, id):
        return True
    
    
    
    