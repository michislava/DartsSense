const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors'); 
const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient({
  log: ['query', 'info', 'warn', 'error'],
});

const app = express();
const port = 9000;

// Middleware o enable CORS
app.use(cors({
  origin: '*'
}));

// Middleware to parse JSON bodies
app.use(express.json());

app.post('/register', async (req, res) => {
  const { firstname, lastname, username, email, pass, skill } = req.body;

  if (!firstname || !lastname || !username || !email || !pass || !skill) {
    return res.status(400).json({ message: 'All fields are required' });
  }

  try {
    const newUser = await prisma.user.create({
      data: {
        firstName: firstname,
        lastName: lastname,
        username,
        email,
        password: pass,
        skillLevel: skill,
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

app.post('/create-game', async (req, res) => {
  try {
    const { name, player1Username, player2Username } = req.body;

    // Ensure all required fields are provided
    if (!name || !player1Username || !player2Username) {
      return res.status(400).json({ error: 'Name and usernames for both players are required' });
    }

    // Find user IDs for both players
    const player1 = await prisma.user.findUnique({
      where: {
        username: player1Username,
      },
    });

    const player2 = await prisma.user.findUnique({
      where: {
        username: player2Username,
      },
    });

    // Ensure both players exist
    if (!player1 || !player2) {
      return res.status(404).json({ error: 'One or both of the players do not exist' });
    }

    // Create a new game with player IDs and the game name
    const newGame = await prisma.game.create({
      data: {
        name,
        player1Id: player1.userId,
        player2Id: player2.userId,
      },
    });

    console.log('Game created successfully:', newGame);

    res.status(200).json({ message: 'Game created successfully', game: newGame });
  } catch (error) {
    console.error('Error creating game:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});


app.post('/esp-data', async (req, res) => {
  console.log(req.body);
  try {
    const { points, throws } = req.body;
    if (!points || !throws) {
      return res.status(400).send('Points and throws (3 throws) are required');
    }

    const playerNames = ['Player 1', 'Player 2', 'Player 3', 'Player 4'];

    const createdPlayers = [];
    for (let i = 0; i < 4; i++) {
      const playerName = playerNames[i];
      const playerScores = throws[i].slice(0, 3); // Take first 3 throws
      const player = await prisma.player.create({
        data: {
          name: playerName,
          scores: playerScores,
        },
      });
      createdPlayers.push(player);
    }
    console.log('Players with throws added to the database:', createdPlayers);

    res.status(200).send('Players with throws added to the database successfully');
  } catch (error) {
    console.error('Error adding players with throws to the database:', error);
    res.status(500).send('Internal server error');
  }
});


// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
