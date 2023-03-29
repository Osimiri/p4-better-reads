import React, { useEffect, useState } from "react";
import Book from "./Book"

function BookPage({books, genre}){
  const bookCards = books.map((book)=> {
    console.log(book)
    // console.log(genre)
    return (
      <Book
        title={book.title}
        price={book.price}
        isbn={book.isbn}
        likes={book.likes}
        genre={book.genre?.genre}
        author={book.author.full_name}
        image = {book.image}
      />
    );
  });
  return <ul>{bookCards}</ul>
}

export default BookPage;
