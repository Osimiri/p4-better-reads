import React, { useEffect, useState } from "react";

function Book({title, price, likes, genre_id, author_id}) {
    return (
      <div>
        <h2>{title}</h2>
        <p>Price: {price}</p>
        <p>Likes: {likes}</p>
        <p>Genre ID: {genre_id}</p>
        <p>Author ID: {author_id}</p>
      </div>
    );
  }

export default Book;