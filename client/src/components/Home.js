import React, { useEffect, useState } from "react";

function Home() {
  // Code goes here!
const [bookArray, setBookArray] = useState([])

useEffect(() => {
  fetch("/")
  .then(res => res.json())
  .then(data => setBookArray(data))
},
[]);
    return (
        <section>
            <h2>Better Reads</h2>
        </section>

    )
       
}

export default Home;