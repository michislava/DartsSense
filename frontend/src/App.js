import './App.css';
import React from 'react';
import LoginForm from './Pages/Login';
import Scores from './Pages/Scores';
import Stats from './Pages/Stats';
import Help from './Pages/Help';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';


function App() {
  return (
    <Router>
      <div className="App">
        <nav>
            <li><Link to="/">Login</Link></li>
            <li><Link to="/scores">Scores</Link></li>
            <li><Link to="/stats">Stats</Link></li>
            <li><Link to="/help">Help</Link></li>
        </nav>
        <Routes>
        <Route path="/" component={LoginForm} />
        
        <Route path="/scores" component={Scores} />
        <Route path="/stats" component={Stats} />
        <Route path="/help" component={Help} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;