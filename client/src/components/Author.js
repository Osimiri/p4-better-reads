import React, { useEffect, useState } from "react";


function Author() {
    return (
      <div>
        <h1>Authors</h1>
        <ul>
          {authors.map((author) => (
            <li>
              <h2>{author.full_name}</h2>
              <p>{author.biography}</p>
            </li>
          ))}
        </ul>
      </div>
    );
  }
  
  export default Author;