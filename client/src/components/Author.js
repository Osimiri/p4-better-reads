import React, { useEffect, useState } from "react";


function Author({full_name, biography, author_image}) {
    return (
        <li>
            <h2>{full_name}</h2>
            <p>{biography}</p>
            <img src={author_image} />
        </li>
    );
  }
  
  export default Author;

  
