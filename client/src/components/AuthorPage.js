import React, { useEffect, useState } from "react";
import Author from "./Author"

function AuthorPage({authors}){
    const authorCards = authors.map((author) => {
        return (
            <Author
            full_name = {author.full_name}
            biography = {author.biography}
            />
        );
    });
    return <ul> {authorCards} </ul>
}

export default AuthorPage