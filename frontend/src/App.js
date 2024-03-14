import './App.css';
import React, { useState, createContext } from 'react';
import RegistrationForm from './Pages/Registration';
import LoginForm from './Pages/Login';
import Main from './Pages/Main';
import Scores from './Pages/Scores';
import Stats from './Pages/Stats';
import Help from './Pages/Help';
import Navbar from './Functions/Navbar';
import Navbar2 from './Functions/Navbar2';
import { BrowserRouter as Router, Route, Routes, Link} from 'react-router-dom';

export const MyContext = createContext();

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLinkClick = () => {
    setIsLoggedIn(true);
    console.log(isLoggedIn)
  // Toggle the state from true to false or false to true
  };

  if (isLoggedIn === false) { 
    return (
      <Router>  
        <div className="App">
          <Navbar>
              <li><Link to="/">Main</Link></li>
              <li><Link to="/scores">Scores</Link></li>
              <li><Link to="/stats">Stats</Link></li>
              <li><Link to="/help">Help</Link></li>
              <li><Link to="/registration">Registration</Link></li>
              <li><Link to="/login">Login</Link></li>
          </Navbar>
          <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/scores" element={<Scores />}/>
          <Route path="/stats" element={<Stats />} />
          <Route path="/help" element={<Help />} />
          <Route path="/registration" element={<RegistrationForm />} />
          <Route path="/login" element={<MyContext.Provider value={{isLoggedIn, setIsLoggedIn}}><LoginForm /> </MyContext.Provider>} />
          </Routes>
        </div>
      </Router>
    );
    }

    if (isLoggedIn === true) { 
      return (
        <Router>
          <div className="App">
            <Navbar2>
                <li><Link to="/">Main</Link></li>
                <li><Link to="/scores">Scores</Link></li>
                <li><Link to="/stats">Stats</Link></li>
                <li><Link to="/help">Help</Link></li>
                <li><Link to="/registration">Registration</Link></li>
                <li><Link to="/login">Login</Link></li>
            </Navbar2>
            <Routes>
            <Route path="/" element={<Main />} />
            <Route path="/scores" element={<Scores />}/>
            <Route path="/stats" element={<Stats />} />
            <Route path="/help" element={<Help />} />
            <Route path="/registration" element={<RegistrationForm />} />
            <Route path="/login" element={<LoginForm />} />
            </Routes>
          </div>
        </Router>
      );
      }
}

export default App;