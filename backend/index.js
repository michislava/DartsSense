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
app.use(cors());

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Your routes
app.post('/register', (req, res) => {
  const { username, email, password } = req.body;
  if (!username || !email || !password) {
      return res.status(400).json({ message: 'All fields are required' });
  }

  // Your registration logic
});

app.post('/login', (req, res) => {
  const { username, password } = req.body;

  // Your login logic
  if (username === 'example' && password === 'password') {
    res.status(200).send('Login successful');
  } else {
    res.status(401).send('Unauthorized');
  }
});

app.post('/esp-data', async (req, res) => {
  const { player, zone } = req.body;

  if (player === undefined || zone === undefined) {
      return res.status(400).json({ error: 'Player and zone are required' });
  }

  try {
      const newGame = await prisma.game.create({
          data: {
              player: player,
              zone: zone
          }
      });
      console.log('Inserted game:', newGame);

      res.status(200).json({ message: 'Data received and saved successfully' });
  } catch (error) {
      console.error('Error inserting game:', error);
      res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
