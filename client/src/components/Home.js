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
          {/* <div className = "header">
            <img className ="logo" src = "Better.jpg" alt = "logo" />
        </div> */}
          <h1>Welcome to Better Reads</h1>
        </section>

    )
}

export default Home;
