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
  const { username, password, skill } = req.body;

  if (!username || !password || !skill) {
    return res.status(400).json({ message: 'All fields are required' });
  }

  try {
    const newUser = await prisma.user.create({
      data: {
        username,
        password,
        skill,
      },
    });

    console.log('User registered successfully:', newUser);

    res.status(200).json({ message: 'User registered successfully', user: newUser });
  } catch (error) {
    console.error('Error registering user:', error);
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
  console.log(req.body);
  console.log(req);
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
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
