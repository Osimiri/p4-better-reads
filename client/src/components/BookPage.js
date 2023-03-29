import React, { useEffect, useState } from "react";
import Book from "./Book"

function BookPage({books}){
  const bookCards = books.map((book)=> {
    return (
      <Book
        title={book.title}
        price={book.price}
        isbn={book.isbn}
        likes={book.likes}
        genre_id={book.genre_id}
        author_id={book.author_id}
        image={book.image}
      />
    );
  });
}

export default BookPage;