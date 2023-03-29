#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc


# Remote library imports
from faker import Faker
from faker.providers import  person, profile, isbn, internet   
# Local imports
from app import app
from models import Author, Genre, User, UserBook, Book, db

fake = Faker()
fake.add_provider(profile)
fake.add_provider(isbn)
fake.add_provider(internet)


def make_genre():
    
    Genre.query.delete()

    genres = ['Drama', 'Fable', 'Fiction', 'Folklore', 'Historical Fiction', 'Horror', 'Mystery',
    'Poetry', 'Science Fiction', 'Non-Fiction', 'Biography', 'Autobiography', 'Art','Romance', 
    'Travel', 'Classics']

    genre_obj = []

    for i in range(len(genres)):
    # for i in range(10):
        genre = Genre(
            genre = genres[i]         
        )

        genre_obj.append(genre)
    
    db.session.add_all(genre_obj)
    db.session.commit()

def make_author():

    Author.query.delete()

    authors = ["Brandon Sanderson", "James Patterson", "Ruth Benedict", 
    "bell hooks", "Laura Purcell", "Action Bronson", "Mark Twain", "Brent Weeks", 
    "Andrew Loomis", "Colleen Hoover", "Chris Bohjalian", "Chuck Tingle", "Blanka Lipińska",
    "Khaled Hosseini", "Chimamanda Ngozi Adichie", "Fonda Lee", "Lucy Maud Montgomery",
    "Hanya Yanagihara", "Toshikazu Kawaguchi", "Susan Hill", "Agatha Christie", "Mary Shelley",
    "Neal Stephenson","Sandle Brandleman"]


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
    # Book.query.filter_by(id=).first()
    # len(Book.query.get(1).liked_books), author_id="1"
    # Book(title="", price="", isbn="", likes="0", author_id="", genre_id="", image = "" )
    books_obj = [
    Book(title="The Way of Kings", price="8.88", isbn="9780765365279", likes="0", author_id="1", genre_id="9", image = "https://d3525k1ryd2155.cloudfront.net/h/014/102/1299102014.0.x.jpg"),
    Book(title="The Angel Experiment: A Maximum Ride Novel", price="4.05", isbn="9780316067959", likes="0", author_id="2", genre_id="3", image = "https://m.media-amazon.com/images/W/IMAGERENDERING_521856-T1/images/I/91Td2ZvUGzL._AC_UF1000,1000_QL80_.jpg"),
    Book(title="Ruth Benedict: Patterns of a Life", price="4.39", isbn="9780812211757", likes="0", author_id="3", genre_id="", image = "https://m.media-amazon.com/images/W/IMAGERENDERING_521856-T1/images/I/41xRR-i323L._AC_UF1000,1000_QL80_.jpg"),
    Book(title="All About Love: New Visions", price="13.12", isbn="9780060959470", likes="0", author_id="4", genre_id="", image = "https://m.media-amazon.com/images/W/IMAGERENDERING_521856-T1/images/I/71xEY+ZI8kL._AC_UF1000,1000_QL80_.jpg" ),
    Book(title="The House of Whispers: A Novel", price="5.05", isbn="9780143135531", likes="0", author_id="5", genre_id="", image = "https://m.media-amazon.com/images/I/41XosKSpLSL.jpg"),
    Book(title="Fuck, That's Delicious", price="19.32", isbn="9781419726552", likes="0", author_id="6", genre_id="", image = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.com%2FThats-Delicious-Annotated-Guide-Eating%2Fdp%2F1419726552&psig=AOvVaw1V6P8Cj89I-jApAAnhX4Wz&ust=1680119752675000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCPCQkfuz__0CFQAAAAAdAAAAABAE"),
    Book(title="The Adventures of Huckleberry Finn", price="4.47", isbn="9780553210798", likes="0", author_id="7", genre_id="", image = "https://www.freedomtoread.ca/wp-content/uploads/twain-adventures-of-huckleberry-finn.jpg"),
    Book(title="The Black Prism (Lightbringer, 1)", price="5.77", isbn="", likes="0", author_id="8", genre_id="", image = "https://i5.walmartimages.com/asr/b6cde832-24cd-4d03-a285-670d2488950e.c6adfef5a67afcd107951faf4e52a8ef.jpeg"),
    Book(title="Fun With A Pencil: How Everybody Can Easily Learn to Draw", price="13.47", isbn="9781805472698", likes="0", author_id="9", genre_id="", image = "https://m.media-amazon.com/images/W/IMAGERENDERING_521856-T1/images/I/61Gmw2eIXYL._AC_UF1000,1000_QL80_.jpg"),
    Book(title="Verity", price="3.19", isbn="9781538724736", likes="0", author_id="10", genre_id="14", image = "https://www.colleenhoover.com/wp-content/uploads/2023/01/Screen-Shot-2023-01-25-at-1.49.58-PM.png"),
    Book(title="Midwives (Oprah's Book Club)", price="3.46", isbn="9780375706776", likes="0", author_id="11", genre_id="", image ="https://sdi2.chrislands.com/sdi/978/03/75/7/9780375706776.jpg"),
    Book(title="Space Raptor Butt Invasion", price=".74", isbn="", likes="0", author_id="12", genre_id="", image = "https://m.media-amazon.com/images/I/51XR3M4I5UL.jpg"),
    Book(title="365 Days", price="12.21", isbn="9781982174309", likes="0", author_id="13", genre_id="16", image = "https://d28hgpri8am2if.cloudfront.net/book_images/onix/cvr9781797124032/365-days-9781797124032_hr.jpg"),
    Book(title="A Thousand Splendid Suns", price="4.04", isbn="9781594489501", likes="0", author_id="14", genre_id="", image= "https://pictures.abebooks.com/isbn/9781594489501-us-300.jpg"),
    Book(title="Americanah", price="4.62", isbn="9780307455925", likes="0", author_id="15", genre_id="10", image = "https://pictures.abebooks.com/isbn/9780307455925-us-300.jpg"),
    Book(title="Exo", price="3.46", isbn="9781338232035", likes="0", author_id="16", genre_id="9", image = "https://pictures.abebooks.com/isbn/9781338232035-us-300.jpg"),
    Book(title="Anne of Green Gables", price="4.38", isbn="9781613822265", likes="0", author_id="17", genre_id="3", image ="https://th.bing.com/th/id/R.0095b42e01d8ce30f8988799f6c3c56a?rik=4v9GY6Vq7GUmlw&pid=ImgRaw&r=0"),
    Book(title="A Little Life", price="12.32", isbn="9780804172707", likes="0", author_id="18", genre_id="1", image = "https://img.lareviewofbooks.org/unsafe/1280x0/filters:format(jpeg)/https%3A%2F%2Fdev.lareviewofbooks.org%2Fwp-content%2Fuploads%2F2015%2F12%2FLittle-Life.png"), 
    Book(title="Before the Coffee Gets Cold", price="7.99", isbn="9781529029581", likes="0", author_id="19", genre_id="3", image = "https://www.westonpubliclibrary.org/main/wp-content/uploads/before-coffee-gets-cold-1351x2048.jpg" ),
    Book(title="The Woman in Black: A Ghost Story", price="4.92", isbn="9780307745316", likes="0", author_id="20", genre_id="6", image = "https://pictures.abebooks.com/isbn/9780307745316-us.jpg" ),
    Book(title="The ABC Murders", price="10.86", isbn="9780007527533", likes="0", author_id="21", genre_id="7", image = "https://th.bing.com/th/id/OIP.ouY5xWd5NVtERCJHQOnnnAHaL9?w=115&h=180&c=7&r=0&o=5&dpr=2&pid=1.7"),
    Book(title="Miss Marple: The Complete Short Stories", price="5.19", isbn="9780425094860", likes="0", author_id="21", genre_id="7", image = "https://th.bing.com/th/id/R.15c8b91e13c858221560f7452a00e0c1?rik=vUSoqQXxo6eh2g&riu=http%3a%2f%2fimg1.imagesbn.com%2fp%2f9780425094860_p0_v1_s260x420.jpg&ehk=nE596TWc3iANmsiaNMPkRHpi7xVXXAh0auL3vV%2fPmyc%3d&risl=&pid=ImgRaw&r=0"),
    Book(title="Frankenstein", price="5.99", isbn="9780486282114", likes="0", author_id="22", genre_id="9", image = "https://th.bing.com/th/id/OIP.iktnpmieggzfcHUS9zfpewHaL_?w=194&h=315&c=7&r=0&o=5&dpr=2&pid=1.7"),
    Book(title="Snow Crash", price="14.19", isbn="0553380958", likes="0", author_id="23", genre_id="9", image = "https://th.bing.com/th/id/OIP.aFTzG9X5pVYRHvJfr47Z7QHaLF?w=194&h=290&c=7&r=0&o=5&dpr=2&pid=1.7"),
    Book(title="Elden Rings: What Should Have Been", price="79.99", isbn="9780420282169", likes="0", author_id="24", genre_id="4", image = "https://media.wired.com/photos/6418c4b05842f211652a9fbf/master/pass/Sanderson-DSCF2575.jpg" )
    ]
    
    # can we add the img src to the []
    
    # books_obj = []

    # for i in range(23):
    # # for i in range(10):
    
    #     book = Book(
    #         title= fake.name(),
    #         price= randint(0,999),
    #         # isbn= fake.isbn(),
    #         likes= randint(1,69),        
    #         genre_id= randint(1,9),
    #         # author_id= randint(1,23)
    #         author_id= i
    #     )

        # books_obj.append(book)
    
    db.session.add_all(books_obj)
    db.session.commit()

def make_user():
    
    User.query.delete()

    users_obj = []

    for i in range(23):
    # for i in range(10):
    
        user = User(
            password= randint(1,23) ,
            username= fake.email(),
            full_name= fake.name(),   
        )

        users_obj.append(user)
    
    db.session.add_all(users_obj)
    db.session.commit()

def make_users_books():
    
    UserBook.query.delete()

    users_books_obj = []

    for i in range(23):
    # for i in range(10):
    
        user_books = UserBook(
            # user_id = randint(1,23),
            user_id = i,
            book_id = randint(1,23)  
        )

        users_books_obj.append(user_books)
    
    db.session.add_all(users_books_obj)
    db.session.commit()

    for book in Book.query.all():
        book.likes = len(book.liked_books)
        
        db.session.add(book)
        db.session.commit()


if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        make_author()
        make_book()
        make_user()
        make_genre()
        make_users_books()
        book = db.session.get(Book,1)
        print(book)
        print(len(book.liked_books))
        # print(len(Book.query.get(1).liked_books))
