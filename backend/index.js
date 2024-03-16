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

app.post('/login', async (req, res) => {
  const { username, password } = req.body;

  try {
    const user = await prisma.user.findUnique({
      where: {
        username: username,
      },
    });

    if (!user) {
      return res.status(401).send('Unauthorized');
    }

    const passwordMatch = user.password === password;

    if (passwordMatch) {
      res.status(200).send('Login successful');
    } else {
      res.status(401).send('Unauthorized');
    }
  } catch (error) {
    console.error('Error logging in:', error);
    res.status(500).send('Internal server error');
  }
});

app.post('/esp-data', async (req, res) => {
  try {
      const { points, throws } = req.body;
      if (!points || !throws || throws.length !== 3) {
          return res.status(400).send('Points and throws (3 throws) are required');
      }

      const playerNames = ['Player 1', 'Player 2', 'Player 3', 'Player 4'];

      const createdPlayers = [];
      for (let i = 0; i < 4; i++) {
          const player = await prisma.player.create({
              data: {
                  name: playerNames[i],
                  throws: {
                      create: throws.map(score => ({ score })),
                  },
              },
              include: {
                  throws: true,
              },
          });
          createdPlayers.push(player);
      }

      console.log('Players and their throws created:', createdPlayers);

      res.status(200).send('Players and their throws added to the database successfully');
  } catch (error) {
      // Log and send an error response if an error occurs
      console.error('Error adding players and throws to the database:', error);
      res.status(500).send('Internal server error');
  }
});



// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
