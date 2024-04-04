<template>
  <div class="about">
    <AboutPage />
  </div>
</template>

<script>
import AboutPage from "../components/AboutPage.vue"
export default {
  components: {
    AboutPage
  }
}
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
