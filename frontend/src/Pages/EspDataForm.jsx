import React, { useEffect } from 'react';
import axios from 'axios';

const Data = () => {
  useEffect(() => {
    const handleMessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        // Check if the received message matches the expected format
        if (data && typeof data === 'object' && 'player' in data && 'zone' in data) {
          axios.post('backend/esp-data', data)
            .then(() => {
              console.log('Data received and saved successfully');
            })
            .catch((error) => {
              console.error('Error sending data to the backend:', error);
            });
        }
      } catch (error) {
        console.error('Error parsing JSON message:', error);
      }
    };
    // Replace 'ws://localhost:8080' with the appropriate WebSocket URL
    const ws = new WebSocket('ws://localhost:80');
    ws.addEventListener('message', handleMessage);

    // Clean up function
    return () => {
      ws.removeEventListener('message', handleMessage);
      ws.close();
    };
  }, []);

  return (
    <div>
      <h1>React App</h1>
      <p>This component listens for JSON messages and sends them to the backend.</p>
    </div>
  );
};

export default Data;
