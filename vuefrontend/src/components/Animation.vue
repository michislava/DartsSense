<template>
  <div>

    <div class="fadeText" :class="{ 'visible': isVisible }">
      <h1>DartsSense</h1>
    </div>

    <div className="Board">
      <img src="../assets/images/BoardReal.png" alt="Sample" />
    </div>

    <Dart :startX=1980 :startY=-100 :endX=-530 :endY=500 />
    <Dart :startX=1980 :startY=-100 :endX=-470 :endY=220 />
    <Dart :startX=1980 :startY=-100 :endX=-370 :endY=110 />
  </div>
</template>

<script>
import Dart from "./Dart.vue"
export default {
    name: 'Animation',
    components: {
        Dart
    },
    data() {
     return {
        isVisible: false
      };
    },
    mounted() {
    // Trigger the fade-in animation after a delay to allow the component to render
    setTimeout(() => {
      this.isVisible = true;
      console.log("benson");
    }, 3000); // 3 seconds delay
  }
}

</script>

<style scoped>
  @keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
  }

  .Board {
    width: 500px; /* Adjust width and height as needed */
    height: 500px;
    position: relative;
    z-index: -1;
    top: 140px; /* Adjust top position as needed */
    left: -700px;
  }

  .visible {
    opacity: 1;
  }

  .fadeText {
    opacity: 0;

    font-size: 80px;
    justify-content: absolute;
    font-weight: 1;
    color: #f3d99b;
    animation: fadeIn 1.5s ease forwards;
    animation-delay: 4.5s;
    position: relative;
    margin-top: 30px;
    top: 50px;
}
</style>
