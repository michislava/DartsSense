import React, { useState } from 'react';
import axios from 'axios';
import './Registration.css';

function RegistrationForm() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [skill_level, setSkill] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await axios.post(`/register`, {
        username,
        email,
        password,
        skill_level
      });
      
      console.log('Registration successful:', response.data);
    } catch (error) {
      console.error('Error registering user:', error);
    }
  };

  return (
    <div className="registration">
      <h1>Registration</h1>
      <form onSubmit={handleSubmit}>
        <div className="username">
          <label>Username: </label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div className="email">
          <label>Email: </label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
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
            value={skill_level}
            onChange={(e) => setSkill(parseInt(e.target.value))}
          />
        </div>
        <div className="Button">
          <button className="button" type="submit">Register</button>
        </div>
      </form>
    </div>
  );
}

export default RegistrationForm;
