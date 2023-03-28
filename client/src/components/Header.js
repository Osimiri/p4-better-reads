import React from 'react'
import {NavLink} from "react-router-dom";

function Header() {
    return(
    <header>
        <div>
            <h1> Header</h1>
        </div>

        <div classname = 'nav'>
        <nav>
            <div className="Route Buttons">
            <NavLink exact to="/" activeClassName="active-nav-link" className="nav-btn">
            <span>Home</span>
            </NavLink>
            <NavLink exact to="/books" activeClassName="active-nav-link" className="nav-btn">
            <span>Books</span>
            </NavLink>
            <NavLink exact to="/authors" activeClassName="active-nav-link" className="nav-btn">
            <span>Authors</span>
            </NavLink>
            <NavLink exact to="/profile" activeClassName="active-nav-link" className="nav-btn">
            <span>Profile</span>
            </NavLink>
            </div>
        </nav>

        </div>
    </header>
    )
}
export default Header;