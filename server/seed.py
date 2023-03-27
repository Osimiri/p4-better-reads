#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc


# Remote library imports
from faker import Faker
from faker.providers import  person   
# Local imports
from app import app
from models import Author, Genre, User, UserBook, Book, db

fake = Faker()

def make_Genre():
    
    Genre.query.delete()

    genre_obj = ['Drama', 'Fable', 'Fiction', 'Folklore', 'Historical Fiction', 'Horror', 'Mystery',
    'Poetry', 'Science Fiction']

    for i in range(len(genre_obj)):
    # for i in range(10):
        genre = Genre(
            genre = genre_obj[i] ,
               
        )

        genre_obj.append(genre)
    
    db.session.add_all(genre_obj)
    db.session.commit()

def make_author():

    Author.query.delete()

    authors = ["Branden Sanderson", "James Patterson", "Ruth Benedict", 
    "bell hooks", "Laura Purcell", "Action Bronson", "Mark Twain", "Brent Weeks", 
    "Andrew Loomis", "Coleen Hoover", "Chris Bohjalian", "Chuck Tingle", "Blanca Lepinska",
    "Khaled Hosseini", "Chimamanda Ngozi Adichie", "Fonda Lee", "Lucy Maud Montgomery",
    "Hanya Yanagihara", "Toshikazu Kawaguchi", "Susan Hill", "Agatha Christie", "Mary Shelley",
    "Neal Stevenson"]


    author_obj = []

    for i in range(len(authors)):
    # for i in range(10):
    
        author = Author(
            full_name= authors[i],
            biography= fake.text()
        )

        author_obj.append(author)


    
    db.session.add_all(author_obj)
    db.session.commit()



def make_book():
    
    Book.query.delete()

    books_obj = []

    for i in range(23):
    # for i in range(10):
    
        book = Book(
            title= fake.name(),
            price= randint(0,999),
          # isbn= fake.isbn(),
            likes= randint(1,69),        
            genre_id= randint(1,9),
            # author_id= randint(1,23)
            author_id= i
        )

        books_obj.append(book)
    
    db.session.add_all(books_obj)
    db.session.commit()

def make_user():
    
    User.query.delete()

    users_obj = []

    for i in range(23):
    # for i in range(10):
    
        user = User(
            password= randint(1,23) ,
            username= fake.name(),
            full_name= fake.name(),   
        )

        users_obj.append(user)
    
    db.session.add_all(users_obj)
    db.session.commit()

def make_users_books():
    
    User.query.delete()

    users_books_obj = []

    for i in range(23):
    # for i in range(10):
    
        user_books = UserBook(
            user_id = randint(1,23),
            book_id = randint(1,23)  
        )

        users_books_obj.append(user_books)
    
    db.session.add_all(users_books_obj)
    db.session.commit()

    




if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        make_author()
        make_book()
        make_users_books()
        make_user()
