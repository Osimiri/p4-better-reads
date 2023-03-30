
import React, { useEffect, useState } from "react";
import {Link} from 'react-router-dom';
import Book from "./Book";
import {Card} from "semantic-ui-react";

function BookPage({books, genre}){
  const bookCards = books.map((book)=> {
    // console.log(book)
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

  return (
    <Card.Group itemsPerRow={4}>
      {bookCards}
    </Card.Group>
  )



}

export default BookPage;