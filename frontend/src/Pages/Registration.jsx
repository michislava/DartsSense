import React, { useState } from 'react';
import './Registration.css';
import axios from 'axios'

function RegistrationForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [skill, setSkill] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Username:', username);
    console.log('Password:', password);
  };

  return (
    <div className="registration">
      <h2>Registration</h2>
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
        <div className="skillLevel">
          <label>Skill level: </label>
          <input
            type="text"
            value={skill}
            onChange={(e) => setSkill(e.target.value)}
          />
        </div>
        <div className="button">
        <button type="submit">Register</button>
        </div>
      </form>
    </div>
  );
}

export default RegistrationForm;