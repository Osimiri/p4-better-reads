import React, { useEffect, useState } from "react";


function Author({full_name, biography}) {
    return (
        <li>
            <h2>{full_name}</h2>
            <p>{biography}</p>
        </li>
    );
  }
  
  export default Author;

  
