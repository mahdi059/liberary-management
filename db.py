import sqlite3

class Book:
    def __init__(self, book_name, author_id, year_of_release):
        self.book_name = book_name
        self.author_id = author_id
        self.year_of_release = year_of_release

class Author:
    def __init__(self, authors_name):
        self.authors_name = authors_name

class Member:
    def __init__(self, member_name):
        self.member_name = member_name

class Library:
    def __init__(self, db_name="db.sqlite3"):
        self.db = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.db:
            self.db.execute(
                """CREATE TABLE IF NOT EXISTS books(
                book_id INTEGER PRIMARY KEY,
                book_name TEXT NOT NULL,
                authors_id INTEGER NOT NULL,
                year_of_release INTEGER,
                FOREIGN KEY (authors_id) REFERENCES authors(aouthors_id)
            )"""
            )

            self.db.execute(
                """CREATE TABLE IF NOT EXISTS authors(
                authors_id INTEGER PRIMARY KEY,
                authors_name TEXT NOT NULL
            )"""
            )

            self.db.execute(
                """CREATE TABLE IF NOT EXISTS members(
                id INTEGER PRIMARY KEY,
                members_name TEXT NOT NULL
            )"""
            )
    # book
    def add_books(self , book):
        with self.db:
            self.db.execute(" INSERT INTO books (book_name , authors_id , year_of_release) VALUES (?,?,?) ",
                            (book.book_name, book.author_id, book.year_of_release))
    
    def update_book(self, update_book , book_id):
        with self.db:
            self.db.execute("UPDATE books SET book_name = ?, authors_id = ?, year_of_release = ? WHERE book_id = ?",
                              (update_book.book_name, update_book.author_id, update_book.year_of_release, book_id))
            
    def delete_book(self, book_id):
        with self.db:
            self.db.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
       
    def all_books_from_authors(self , authors_id):
        query = """ SELECT books.book_name,
                            authors.authors_name,
                            books.year_of_release
                            FROM books
                            JOIN authors ON books.authors_id = authors.authors_id
                            WHERE authors.authors_id =? """
        with self.db:
           result = self.db.execute(query , (authors_id ,))
        for item in result:
            print(item)

    def all_books_and_authors(self):
        with self.db:
            query = (""" SELECT books.book_name,
                            authors.authors_name,
                            books.year_of_release
                            FROM books 
                            JOIN authors ON books.authors_id = authors.authors_id """)
            with self.db:
                result = self.db.execute(query)

                for item in result:
                    print(item)

    def show_id_and_name(self):
        with self.db:
          result = self.db.execute("SELECT book_id , book_name FROM books")

          for item in result:
              print(item)

    # authors
    def add_authors(self , author ):
        with self.db:
            self.db.execute(" INSERT INTO authors (authors_name) VALUES(?)", (author.authors_name ,))

    def update_authors(self ,  update_authors , author_id):
        with self.db:
            self.db.execute("UPDATE authors SET authors_name = ? WHERE authors_id = ?", (update_authors.authors_name, author_id))

    def delete_authors(self , author_id):
        with self.db:
            self.db.execute(" DELETE FROM authors WHERE authors_id = ? ", (author_id ,))
        
    def show_authors(self):
        with self.db:
          result = self.db.execute("SELECT * FROM authors")

          for item in result:
              print(item)
    # members          
    def add_members(self , member):
        with self.db:
            self.db.execute(" INSERT INTO members (members_name) VALUES(?)", (member.member_name ,))

    def update_members(self , member , member_id):
        with self.db:
            self.db.execute(" UPDATE members SET members_name = ? WHERE id = ? ", (member.member_name , member_id))
        
    def delete_members(self , member_id):
        with self.db:
            self.db.execute("DELETE FROM members WHERE id = ?", (member_id ,))

    def show_members(self):
        with self.db:
           result = self.db.execute(" SELECT * FROM members")

           for item in result:
               print(item)

    
    
