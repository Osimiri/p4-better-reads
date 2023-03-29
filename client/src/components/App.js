import React, { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";
import Author from "../components/Author";
import AuthorPage from "../components/AuthorPage";
import Book from "../components/Book";
import BookPage from "../components/BookPage";
import Header from "../components/Header";
import Home from "../components/Home";
import Profile from "../components/Profile";
import User from "../components/User";



function App() {
  
  const [authors, setAuthors] = useState([]);
  const [books, setBooks] = useState([]);


  useEffect(() => {
    fetch("http://localhost:4000/books")       // link for the books DB
      .then((res) => res.json())
      .then((data) => setBooks(data));
  }, []);

  useEffect(() => {
    fetch("http://localhost:4000/author/")       // link for the authors DB
      .then((res) => res.json())
      .then((data) => setAuthors(data));
  }, []);
  
   
  
  return(
      <div className="App">
      <Header />
        <h1>Welcome to Better Reads</h1>

        <Routes>
          <Route path="/" element={<Home />} /> 
          <Route path="/books" element={<BookPage books = {books} />} /> 
          <Route path="/authors" element={<AuthorPage authors = {authors}/>} /> 
          <Route path="/profile" element={<Profile />} />

        </Routes>


      </div>
  )
}



export default App;

// dont think that we need a component for userbooks, since theyll be rendered after sorting 
// dont think we need genre compnonent since genres link to backend will just be used for sorting i think
// whats difference intended for BookPage vs Render Book component
// I think book is for how each individual book will render on a card 
// but book page is the container they would all live in 

//I wasnt sure, i thought they would be the same thing 
//we can delete 
//so kinda like how pokemon searcher was like?
//yuh
//but we can go ahead and delete genre and userbooks