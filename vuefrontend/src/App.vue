<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AxiosTest from "./components/AxiosTest.vue"
</script>

<template>
  <div class="navbar">
    <div >

      <nav>
        <RouterLink class="navel" to="/">Home</RouterLink>
        <RouterLink class="navel" to="/about">About</RouterLink>
        <RouterLink class="navel" to="/play">Play</RouterLink>
        <RouterLink class="navel" to="/leaderboard">Leaderboard</RouterLink>
        <RouterLink class="navel" to="/register">Register</RouterLink>
        <RouterLink class="navel" to="/login">Log In</RouterLink>
      </nav>
    </div>

  </div>

  <div class="router-view-container">
    <RouterView class="router-view-container"></RouterView>
  </div>
  

</template>

<style>
body { 
  background-color: #433c43; 
}
.navbar {
  background-color: #81aa8e;
  width: 100%;
  top: 0;
  left:0;
  position: fixed;
  align-items: center;  
  text-align: right;
  height: 25px;
}

.navel {
  color: #715656;
  font-weight: bold;
  margin-right: 5px;
}

.navel:hover {
  transition-duration: 0.5s;
  background-color: #8e839b;
}

.navbar ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.navbar ul li {
  display: inline;
}

.navbar ul li a {
  text-decoration: none;
  color: #fff;
  padding: 10px;
}

.navbar ul li a:hover {
  background-color: #555;
}
.router-view-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: fixed;
  margin: 0 0;
  left: 15;
}
</style>