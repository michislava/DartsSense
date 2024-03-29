import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar2() {
  return (
    <nav className="navbar">
      <div className="navbar-logo-main">
        <Link to="/" className="navbar-logo-link">
          DartsSense
        </Link>
      </div>
      <ul className="navbar-nav">
        <li className="nav-item">
          <Link to="/" className="nav-link">Home</Link>
        </li>
        <li className="nav-item">
          <Link to="/leaderboard" className="nav-link">Leaderboard</Link>
        </li>
        <li className="nav-item">
          <Link to="/rules" className="nav-link">Rules</Link>
        </li>
        <li className="nav-item">
          <Link to="/registration" className="nav-link">Register</Link>
        </li>
        <li className="nav-item">
          <Link to="/login" className="nav-link">Login</Link>
        </li>
        <div className="navbar-logo-icon">
          <Link to="/player" className="nav-link">
          Player
          <span className="tooltip">Player info</span>
          </Link>
          
        </div>
      </ul>
    </nav>
  );
}

export default Navbar2;