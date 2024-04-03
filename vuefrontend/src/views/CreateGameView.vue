<template>
    <div class="create-game">
      <GameCreation/>
    </div>
</template>
  
<script setup>
import GameCreation from "../components/GameCreation.vue"
</script>

  <style>
  @media (min-width: 1024px) {
    .about {
      min-height: 100vh;
      display: flex;
      align-items: center;
    }
  }
  </style>
  