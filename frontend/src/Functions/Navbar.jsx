import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';
import logo from '../Assets/dartsLogo1.png';

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo-main">
      <img src={logo} alt="Icon" className="navbar-logo-mainicon"/>
        <Link to="/" className="navbar-logo-link">
          DartsSense
        </Link>
      </div>
      <ul className="navbar-nav">
        <li className="nav-item">
          <Link to="/" className="nav-link">Home</Link>
        </li>
        <li className="nav-item">
          <Link to="/registration" className="nav-link">Registrer</Link>
        </li>
        <li className="nav-item">
          <Link to="/login" className="nav-link">Login</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;