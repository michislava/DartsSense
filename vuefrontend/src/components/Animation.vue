<template>
  <div class="greetings">

    <div className="fadeText">
      <h1>DartsSense</h1>
    </div>

    <div className="Board">
      <img src="../assets/images/BoardReal.png" alt="Sample" />
    </div>

    <Dart :startX=1000 :startY=-100 :endX=-600 :endY=500 />
    <Dart :startX=1000 :startY=-100 :endX=-550 :endY=220 />
    <Dart :startX=1000 :startY=-100 :endX=-450 :endY=110 />
  </div>
</template>

<script>
import Dart from "./Dart.vue"
export default {
    name: 'Animation',
    components: {
        Dart
    },
    
}

</script>

<style scoped>
  
  .flying-dart1 {
    position: absolute;
    width: 60px; /* Adjust width and height as needed */
    height: 40px;
    background-image: url('../assets/images/dart-illustration.png'); /* Use custom image */
    background-size: cover;
    animation: fly 2s linear forwards;
    animation-delay: 0s;
  }

  .Board {
    width: 500px; /* Adjust width and height as needed */
    height: 500px;
    position: relative;
    z-index: -1;
    top: 140px; /* Adjust top position as needed */
    left: -800px;
  }

  .fadeText {
    font-size: 50px;
    justify-content: center;
    color: #FFD700;
    animation: fadeIn 2s;
    position: relative;
    margin-top: 30px;
    left: -50px; /* Move the h1 50 pixels to the right */
    top: 333px; /* Move the h1 20 pixels down */
}
</style>
