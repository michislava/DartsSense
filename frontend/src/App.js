import './App.css';
import React from 'react';
import LoginForm from './Pages/Login';
import Main from './Pages/Main';
import Scores from './Pages/Scores';
import Stats from './Pages/Stats';
import Help from './Pages/Help';
import Navbar from './Functions/Navbar';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';


function App() {
  return (
    <Router>
      <div className="App">
        <Navbar>
            <li><Link to="/">Main</Link></li>
            <li><Link to="/scores">Scores</Link></li>
            <li><Link to="/stats">Stats</Link></li>
            <li><Link to="/help">Help</Link></li>
        </Navbar>
        <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/scores" element={<Scores />}/>
        <Route path="/stats" element={<Stats />} />
        <Route path="/help" element={<Help />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;