import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';
import logo from '../Assets/dartsLogo1.png';

function Navbar2() {
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
          <Link to="/scores" className="nav-link">Scores</Link>
        </li>
        <li className="nav-item">
          <Link to="/stats" className="nav-link">Stats</Link>
        </li>
        <li className="nav-item">
          <Link to="/help" className="nav-link">Help</Link>
        </li>
        <div className="navbar-logo-icon">
          <img src={logo} alt="Info Icon" className="navbar-logo-iconlink"/>
          <span className="tooltip">Login info</span>
        </div>
      </ul>
    </nav>
  );
}

export default Navbar2;