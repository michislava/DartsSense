const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors'); 
const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient({
  log: ['query', 'info', 'warn', 'error'],
});

const app = express();
const port = 9000;

// Middleware to enable CORS
app.use(cors({
  origin: '*'
}));

// Middleware to parse JSON bodies
app.use(express.json());

app.post('/register', async (req, res) => {
  const { username, password, email, skill_level } = req.body;

  if (!username || !password || !email || !skill_level) {
    return res.status(400).json({ message: 'All fields are required' });
  }

  try {
    const newUser = await prisma.user.create({
      data: {
        username,
        password,
        email,
        skill_level,
      },
    });

    console.log('User registered successfully:', newUser);

    res.status(200).json({ message: 'User registered successfully', user: newUser });
  } catch (error) {
    console.error('Error registering user:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/users', async (req, res) => {
  try {
    const allUsers = await prisma.user.findMany();
    res.status(200).json(allUsers);
  } catch (error) {
    console.error('Error fetching users:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.post('/login', (req, res) => {
  const { username, password } = req.body;
  if (username === 'example' && password === 'password') {
    res.status(200).send('Login successful');
  } else {
    res.status(401).send('Unauthorized');
  }
});

app.post('/esp-data', async (req, res) => {
  try {
      const { player, points } = req.body;
      if (player === undefined || points === undefined) {
        return res.status(400).send('Player and points are required');
      }
      console.log(`Player: ${player}, Points: ${points}`);
      res.status(200).send('Data received and processed successfully');
    } catch (error) { 
      console.error('Error parsing JSON:', error);
      res.status(400).send('Invalid JSON data');
    }
    createFinishedGame();
});

async function createFinishedGame() {
  console.log("vleznahme");
  try {
      const newGame = await prisma.game.create({
      data: {
        game_type: 'Finished',
      },
    });

    console.log("tvato stana");

    // Define the player scores and the threshold for winning
    const playerScores = [0, 0, 0, 0];
    const winningScore = 301;

    for (let i = 0; i < 3; i++) {
      for (let player = 0; player < 4; player++) {
        // Generate a random score for each throw between 3 and 50
        const throwScore = Math.floor(Math.random() * (50 - 3 + 1)) + 3; // Random score between 3 and 50
        playerScores[player] += throwScore;

        // Create game result entry for each throw
        await prisma.gameResult.create({
          data: {
            game_id: newGame.game_id,
            user_id: player + 1, // Assuming user IDs start from 1
            score: throwScore,
          },
        });
        console.log("ima li ciganiiiiiiiiiiiii");
        // Check if any player has reached the winning score
        if (playerScores[player] >= winningScore) {
          console.log(`Player ${player + 1} wins!`);
          return;
        }
      }
    }

    console.log('No winner yet!');
  } catch (error) {
    console.error('Error creating finished game:', error);
  }
}


// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
