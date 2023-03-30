import React, { useEffect, useState } from "react";

function Book({title, price, likes, genre, author, image}) {
  // console.log(author)
    return (
      <li>
        <h2>{title}</h2>
        <img src = {image} class='bookImage'/>
        <p>Price: ${price}</p>
        <p>Likes: {likes}</p>
        {genre && <p>Genre: {genre}</p> }
        <p>Author: {author}</p>
      </li>
    );
  }

export default Book;
