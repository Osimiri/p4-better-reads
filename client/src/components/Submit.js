// Form file 
import React, { useState } from "react";
import { Form } from "semantic-ui-react";

function Submit({genres}) {
  
  const [category, setCategoryForm] = useState([]);
  function handleCategory(e) {
    setCategoryForm([...category,e.target.textContent]);
  }

  function handleSubmit(e) {
    e.preventDefault();
    console.log(e.target.User.value)
    console.log(e.target.image.value)
    console.log(e.target.Description.value)
    console.log(e.target.category)
    const newPost = {
      image: e.target.image.value ,
      category: category ,
      user: e.target.User.value ,
      description: e.target.Description.value ,
      likes: 0,
      saved: false,
    };
    e.target.reset();
    // handlePost(newPost);

    fetch("http://localhost:4000/pins", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newPost),
    })
      .then((res) => res.json())
 
  }
  const genreOptions = [
    {genres}
    // { key: "ceramic", text: "Ceramic", value: "ceramic" },
    // { key: "painting", text: "Painting", value: "painting" },
    // { key: "print", text: "Print", value: "print" },
    // { key: "carving", text: "Carving", value: "carving" },
    // { key: "diy", text: "DIY", value: "diy" },
    // { key: "decor", text: "Decor", value: "decor" },
    // { key: "mine", text: "I Made This", value: "mine"},
  ];

  return (
    <div style={{ backgroundColor: "#F5DEB3", borderRadius: "30px", padding: "20px", maxWidth: "800px", margin: "0 auto" }}>
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
            placeholder="Who Wrote This?"
            name="User"
            style={{ borderRadius: "25px" }}
          />
          <Form.Input
          size="small"
            label="ISBN"
            placeholder="Book ISBN-13#"
            name="User"
            style={{ borderRadius: "25px" }}
          />
          <Form.Input
          size="small"
            label="Image"
            placeholder="Image url"
            name="image"
            style={{ borderRadius: "25px" }}
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
        <Form.Button color="red">Submit</Form.Button>
      </Form>
    </div>
  );
}

export default Submit;
