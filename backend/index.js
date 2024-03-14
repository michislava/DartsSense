import { PrismaClient } from '@prisma/client';

const express = require('express');
const bodyParser = require('body-parser');

const prisma = new PrismaClient({
  log: ['query', 'info', 'warn', 'error'],
});

const app = express();
const port = 9000;

// Middleware to parse JSON bodies
app.use(bodyParser.json());

app.post('/register', (req, res) => {
  const { username, email, password } = req.body;
  if (!username || !email || !password) {
      return res.status(400).json({ message: 'All fields are required' });
  }

  if (users.find(user => user.email === email)) {
      return res.status(400).json({ message: 'User with this email already exists' });
  }

  const newUser = { username, email, password };

  users.push(newUser);
  res.status(200).json({ message: 'User registered successfully', user: newUser });
});

app.post('/login', (req, res) => {
  const { username, password } = req.body;

  // Replace this with your actual login logic
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
