<template>
    <div>
      <h2>Player Score Information</h2>
      <p>Player: {{ player }}</p>
      <p>Score: {{ score }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        player: '',
        score: 0
      };
    },
    created() {
      // Hardcoded JSON payload for testing
      const payload = { player: 'player 1', score: 1 };
  
      // Extract player and score from the JSON payload
      this.player = payload.player;
      this.score = payload.score;
  
      // Alternatively, if you want to use Axios to make an HTTP POST request
      // and extract data from the response:
      
      axios.post('api/esp-data', payload)
        .then(response => {
          this.player = response.data.player;
          this.score = response.data.score;
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    }
  };
  </script>