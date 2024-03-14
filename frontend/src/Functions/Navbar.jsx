import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <Link to="/" className="navbar-logo-link">
          Logo
        </Link>
      </div>
      <ul className="navbar-nav">
        <li className="nav-item">
          <Link to="/" className="nav-link">Home</Link>
        </li>
        <li className="nav-item">
          <Link to="/scores" className="nav-link">Scores</Link>
        </li>
        <li className="nav-item">
          <Link to="/stats" className="nav-link">Stats</Link>
        </li>
        <li className="nav-item">
          <Link to="/help" className="nav-link">Help</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;