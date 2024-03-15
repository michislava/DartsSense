import React, { useState } from 'react';
import axios from 'axios';
import './Registration.css';

function RegistrationForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [skill, setSkill] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await axios.post(`${process.env.BACKEND_ADDRESS}/register`, {
        username,
        password,
        skill
      });
      
      console.log('Registration successful:', response.data);
    } catch (error) {
      console.error('Error registering user:', error);
    }
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
