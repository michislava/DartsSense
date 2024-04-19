<template>
    <div class="about">
      <AboutPage />
    </div>
  </template>

<script>
import axios from "axios";
import "../assets/style.css"

export default {

    data() {
    return {
      websocket: null,
    }
    },
    created() {
    // Hardcoded JSON payload for testing
    const payload = { player: 'player1', score: 13 };

    // Send POST request to backend API when component is created
    this.sendScoreToServer(payload);
  },
        methods: {
    async sendScoreToServer(payload) {
      try {
        // Send POST request to your backend API endpoint
        const response = await axios.post('api/esp-data', payload);

        console.log('Server response:', response.data);
        // Handle response if needed
      } catch (error) {
        console.error('Error sending score:', error);
        // Handle error if needed
      }
    },
}
}
</script>   
  