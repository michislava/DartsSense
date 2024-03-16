// Leaderboard.jsx

import React from 'react';
import './Leaderboard.css';

const generateRandomScores = () => {
  // Generate random scores for each player
  const scores = [];
  for (let i = 0; i < 4; i++) {
    const playerScores = [];
    for (let j = 3; j <= 50; j++) {
      playerScores.push(Math.floor(Math.random() * 100)); // Generate random scores from 3 to 100
    }
    scores.push(playerScores);
  }
  return scores;
};

const Leaderboard = () => {
  // Generate random scores for each player
  const playerScores = generateRandomScores();

  return (
    <div className="leaderboard">
      <h1>Leaderboard</h1>
      <table>
        <thead>
          <tr>
            <th>Player</th>
            <th>Scores</th>
          </tr>
        </thead>
        <tbody>
          {playerScores.map((scores, index) => (
            <tr key={index}>
              <td>Player {index + 1}</td>
              <td>{scores.join(', ')}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Leaderboard;
