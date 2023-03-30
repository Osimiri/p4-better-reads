// Form file 
import React, { useState } from "react";
import { Form } from "semantic-ui-react";
// import { useFormik } from "formik";

function Submit({genres}) {
  
  const [genre, setCategoryForm] = useState([]);
  function handleCategory(e) {
    setCategoryForm([...genre,e.target.textContent]);
  }

  function handleSubmit(e) {
    e.preventDefault();
    // console.log(e.target.User.value)
    // console.log(e.target.image.value)
    // console.log(e.target.Description.value)
    // console.log(e.target.category)
    const newPost = {
      title: e.target.title.value ,
      // category: category ,
      user: e.target.User.value ,
      description: e.target.Description.value ,
      likes: 0,
      saved: false,
    };
    e.target.reset();
    // handlePost(newPost);

    fetch("http://localhost:4000/books", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newPost),
    })
      .then((res) => res.json())
 
  }

  // const formik = useFormik({
  //   title: "",
  //   author:'', 
  //   isbn: '',
  //   image_url
  // })

  const genreOptions = [
    // {genres}
    { key: "drama", text: "Drama", value: "drama" },
    { key: "fable", text: "Fable", value: "fable" },
    { key: "fiction", text: "Fiction", value: "fiction" },
    { key: "folklore", text: "Folklore", value: "folklore" },
    { key: "historical fiction", text: "Historical Fiction", value: "historical fiction" },
    { key: "horror", text: "Horror", value: "horror" },
    { key: "mystery", text: "Mystery", value: "mystery"},
    { key: "poetry", text: "Poetry", value: "poetry"},
    { key: "science fiction", text: "Science Fiction", value: "science fiction"},
    { key: "non-fiction", text: "Non-Fiction", value: "non-fiction"},
    { key: "biography", text: "Biography", value: "biography"},
    { key: "autobiography", text: "Autobiography", value: "biography"},
    { key: "art", text: "Art", value: "art"},
    { key: "romance", text: "Romance", value: "romance"},
    { key: "travel", text: "Travel", value: "travel"},
    { key: "classics", text: "Classics", value: "classics"},
    { key: "cookbook", text: "Cookbook", value: "cookbook"},
    { key: "fantasy", text: "Fantasy", value: "fantasy"},
  ];

// Vertical Small Setup for Submit Form 
  return (
    <div style={{ backgroundColor: "#F5DEB3", borderRadius: "30px", padding: "20px", maxWidth: "900px", margin: "0 auto" }}>
      <h3>Submit A New Post</h3>
      <Form  onSubmit={handleSubmit}>
        <Form.Field  widths="equal">
          <Form.Input
            
            size="small"
            label="Book Title"
            placeholder="Book Title"
            name="Description"
            style={{ borderRadius: "25px" }}
          />
          <Form.Input
            
            size="small"
            label="Author"
            placeholder="First Name Last Name"
            name="User"
            style={{ borderRadius: "25px"  }}
          />
          <Form.Input
            
            size="small"
            label="ISBN"
            placeholder="Book ISBN 13"
            name="isbn"
            style={{ borderRadius: "25px"  }}
          />
          <Form.Input
            flid
            size="small"
            label="Image"
            placeholder="Image url"
            name="image"
            style={{ borderRadius: "25px"  }}
          />
          <Form.Select
            
            size="small"
            label="Genre"
            placeholder="figure it out you little idiot"
            name="genre"
            multiple
            options= {genreOptions}
            onChange={handleCategory}
          />
        </Form.Field>
        {/* <Form.Button color="red">
          Submit
        </Form.Button> */}
      </Form>
    </div>
  ); 
}

export default Submit;