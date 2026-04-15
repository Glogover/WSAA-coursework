# boook dao 
# this is a demonstration a data layer that connects to a datbase

import mysql.connector
import dbconfig as cfg

class BookDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.cursor.close()
        self.connection.close()
         
    def getAll(self):
        cursor = self.getcursor()
        sql="select * from book"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []

        for result in results:
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from book where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()

        # FIX: handle None safely
        if result is None:
            self.closeAll()
            return None

        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def create(self, book):
        cursor = self.getcursor()
        sql="insert into book (title,author, price) values (%s,%s,%s)"
        values = (book.get("title"), book.get("author"), book.get("price"))
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        book["id"] = newid
        self.closeAll()
        return book

    def update(self, id, book):
        cursor = self.getcursor()
        sql="update book set title=%s, author=%s, price=%s where id=%s"
        values = (book.get("title"), book.get("author"), book.get("price"), id)

        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

        # FIX: return something so Flask can jsonify it
        return True

    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from book where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

        # FIX: return something so Flask can jsonify it
        return True

    def convertToDictionary(self, resultLine):
        # FIX: handle None safely
        if resultLine is None:
            return None

        attkeys=['id','title','author','price']
        book = {}
        currentkey = 0
        for attrib in resultLine:
            book[attkeys[currentkey]] = attrib
            currentkey += 1
        return book

bookDAO = BookDAO()
