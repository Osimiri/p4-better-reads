import React, {useState} from "react";
import { Card, Image, Button } from "semantic-ui-react";
import Author from "./Author";

function Book({ title, price, likes, genre, author, image, author_image }) {
  
  const [showFront, setShowFront] = useState(true);

  const toggleCard = () => {
    setShowFront(!showFront);
  };

  return (
  <Card className="card-container" onClick={toggleCard}>
    {showFront ? (
      <>
        <Image src={image} alt={title} />
        <Card.Content>
          <Card.Header>{title}</Card.Header>
          <Card.Meta>
            <span className="date">Price: ${price}</span>
        </Card.Meta>
        <Card.Description>
          <p>Likes: {likes}</p>
          {genre && <p>Genre: {genre}</p>}
          <p>Author: {author}</p>
        </Card.Description>
        <div  className="card-button">
          <Button className="button" color="brown">
            Like
          </Button>
        </div>
        </Card.Content>
      </>
    ) : (
      <Card.Content>
        <Card.Description>{author_image}</Card.Description>
    </Card.Content>
  )}
</Card>
);
} 

export default Book;


