const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const jwt = require('jsonwebtoken'); // Import jsonwebtoken
const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient({
  log: ['query', 'info', 'warn', 'error'],
});

const app = express();
const port = 9000;

// Middleware to enable CORS and parse JSON bodies
app.use(cors());
app.use(express.json());

// JWT Secret Key (should be securely stored in environment variable)
const jwtSecretKey = 'your_secret_key';

// Middleware to generate JWT token
function generateToken(userId) {
  return jwt.sign({ userId }, jwtSecretKey, { expiresIn: '1h' }); // Token expires in 1 hour
}

// Middleware to verify JWT token
function verifyToken(req, res, next) {
  const token = req.headers.authorization;

  if (!token) {
    return res.status(401).json({ message: 'Unauthorized - Token not provided' });
  }

  try {
    const decoded = jwt.verify(token, jwtSecretKey);
    req.userId = decoded.userId; // Attach userId to request object
    next(); // Proceed to next middleware or route handler
  } catch (error) {
    return res.status(401).json({ message: 'Unauthorized - Invalid token' });
  }
}

// Register route with token generation
app.post('/api/register', async (req, res) => {
  const { firstname, lastname, username, email, pass, deviceId, skill } = req.body;

  // Validate request body
  if (!firstname || !lastname || !username || !email || !pass || !deviceId || !skill) {
    return res.status(400).json({ message: 'All fields are required' });
  }

  try {
    // Check if the username already exists
    const existingUser = await prisma.user.findUnique({
      where: { username },
    });

    if (existingUser) {
      return res.status(400).json({ error: 'Username already exists' });
    }

    // Create a new user
    const newUser = await prisma.user.create({
      data: {
        firstName: firstname,
        lastName: lastname,
        username,
        email,
        password: pass,
        deviceId,
        skillLevel: skill,
      },
    });

    console.log('User registered successfully:', newUser);

    // Generate JWT token for the registered user
    const token = generateToken(newUser.userId);

    res.status(200).json({ message: 'User registered successfully', user: newUser, token });
  } catch (error) {
    console.error('Error registering user:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Login route with token generation
app.post('/api/login', async (req, res) => {
  const { username, password } = req.body;

  try {
    const user = await prisma.user.findUnique({
      where: { username },
    });

    if (!user) {
      return res.status(401).send('Unauthorized');
    }

    const passwordMatch = user.password === password;

    if (passwordMatch) {
      // Generate JWT token for the authenticated user
      const token = generateToken(user.userId);
      res.status(200).json({ message: 'Login successful', token });
    } else {
      res.status(401).send('Unauthorized');
    }
  } catch (error) {
    console.error('Error logging in:', error);
    res.status(500).send('Internal server error');
  }
});

// Protected route example (requires valid token)
app.get('/api/users', verifyToken, async (req, res) => {
  try {
    const allUsers = await prisma.user.findMany();
    res.status(200).json(allUsers);
  } catch (error) {
    console.error('Error fetching users:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
