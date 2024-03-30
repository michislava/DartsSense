<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div class="navbar">
    <div >
      <nav >
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/register">Register</RouterLink>
        <RouterLink to="/login">Login</RouterLink>
      </nav>
    </div>
  </div>

  <div class="router-view-container">
    <RouterView class="router-view-container"></RouterView>
  </div>

</template>

<style scoped>
.navbar {
  background-color: #fff;
  color: #fff;
  width: 100%;
  padding-top: 20px;
  top: 0;
  left:0;
  position: fixed;
  align-items: center;
  text-align: center;
  height: 30px;
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
  justify-content: center;
  left: 15;
}
</style>
