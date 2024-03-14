import React, { useState, useContext } from 'react';
import './Registration.css';
import axios from "axios"
import { MyContext } from '../App.js';

function LoginForm() {
  const { isLoggedIn, setIsLoggedIn} = MyContext();

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Username:', username);
    console.log('Password:', password);
    setIsLoggedIn(!isLoggedIn)
    }

  return (
    <div className="login">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div className="username">
          <label>Username: </label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div className="pass">
          <label>Password: </label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <div className="button">
        <button type="submit">Login</button>
        </div>
      </form>
    </div>
  );
}

export default LoginForm;