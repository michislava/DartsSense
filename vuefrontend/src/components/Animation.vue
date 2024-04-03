<template>
  <div class="greetings">
    <div className="flying-dart1"></div>
    <div className="flying-dart2"></div>
    <div className="flying-dart3"></div>
    <div className="Board">
      <img src="../assets/images/BoardReal.png" alt="Sample" />
    </div>
    <div className="fadeText">
      <h1>DartsSense</h1>
    </div>
  </div>
</template>

<script>

export default {
    name: 'Animation',
}
</script>

<style scoped>
@keyframes fly {
    0% {
        bottom: 3px;
        right: 1px;
        transform: rotate(-300deg) translateY(0);
      }
      10% {
        bottom: 10%;
        right: 10%;
        transform: rotate(-310deg) translateY(0);
      }
      20% {
        bottom: 20%;
        right: 20%;
        transform: rotate(-320deg) translateY(0);
      }
      30% {
        bottom: 30%;
        right: 30%;
        transform: rotate(-325deg) translateY(0);
      }
      40% {
        bottom: 40%;
        right: 40%;
        transform: rotate(-330deg) translateY(0);
      }
      45% {
        bottom: 45%;
        right: 45%;
        transform: rotate(-333deg) translateY(0);
      }
      50% {
        bottom: 50%;
        right: 50%;
        transform: rotate(-335deg) translateY(0);
      }
      55% {
        bottom: 48%;
        right: 55%;
        transform: rotate(-338deg) translateY(0);
      }
      60% {
        bottom: 45%;
        right: 60%;
        transform: rotate(-340deg) translateY(0);
      }
      70% {
        bottom: 39.8%;
        right: 77.3%;
        transform: rotate(-345deg) translateY(0);
      }
      100% {
        bottom: 39.8%; /* Stay at the same position */
        right: 77.3%;
        transform: rotate(-345deg) translateY(0);
      }
  }

  @keyframes fly2 {
    0% {
        bottom: 30%;
        right: 1%;
        transform: rotate(-300deg) translateY(0);
      }
      10% {
        bottom: 30%;
        right: 10%;
        transform: rotate(-310deg) translateY(0);
      }
      20% {
        bottom: 30%;
        right: 20%;
        transform: rotate(-320deg) translateY(0);
      }
      30% {
        bottom: 30%;
        right: 30%;
        transform: rotate(-325deg) translateY(0);
      }
      40% {
        bottom: 30%;
        right: 40%;
        transform: rotate(-330deg) translateY(0);
      }
      45% {
        bottom: 30%;
        right: 45%;
        transform: rotate(-333deg) translateY(0);
      }
      50% {
        bottom: 30%;
        right: 50%;
        transform: rotate(-335deg) translateY(0);
      }
      55% {
        bottom: 30%;
        right: 60%;
        transform: rotate(-338deg) translateY(0);
      }
      60% {
        bottom: 30%;
        right: 70%;
        transform: rotate(-340deg) translateY(0);
      }
      70% {
        bottom: 30%;
        right: 72%;
        transform: rotate(-340deg) translateY(0);
      }
      100% {
        bottom: 30%; /* Stay at the same position */
        right: 72%;
        transform: rotate(-340deg) translateY(0);
      }
  }

  @keyframes fly3 {
    0% {
        bottom: 50%;
        right: 1%;
        transform: rotate(-300deg) translateY(0);
      }
      10% {
        bottom: 50%;
        right: 10%;
        transform: rotate(-310deg) translateY(0);
      }
      20% {
        bottom: 50%;
        right: 20%;
        transform: rotate(-320deg) translateY(0);
      }
      30% {
        bottom: 50%;
        right: 30%;
        transform: rotate(-325deg) translateY(0);
      }
      40% {
        bottom: 50%;
        right: 40%;
        transform: rotate(-330deg) translateY(0);
      }
      45% {
        bottom: 50%;
        right: 50%;
        transform: rotate(-333deg) translateY(0);
      }
      50% {
        bottom: 50%;
        right: 60%;
        transform: rotate(-335deg) translateY(0);
      }
      55% {
        bottom: 50%;
        right: 70%;
        transform: rotate(-338deg) translateY(0);
      }
      60% {
        bottom: 50%;
        right: 75%;
        transform: rotate(-340deg) translateY(0);
      }
      70% {
        bottom: 50%;
        right: 75%;
        transform: rotate(-345deg) translateY(0);
      }
      100% {
        bottom: 50%; /* Stay at the same position */
        right: 75%;
        transform: rotate(-345deg) translateY(0);
      }
  }

  @keyframes fadeIn {
    0% { opacity: 0; }
    90% { opacity: 0; }
    100% { opacity: 1; }
  }
  
  .flying-dart1 {
    position: absolute;
    width: 60px; /* Adjust width and height as needed */
    height: 40px;
    background-image: url('../assets/images/dart-illustration.png'); /* Use custom image */
    background-size: cover;
    animation: fly 2s linear forwards;
    animation-delay: 0s;
  }

  .flying-dart2 {
    position: relative;
    width: 60px; /* Adjust width and height as needed */
    height: 40px;
    background-image: url('../assets/images/dart-illustration.png'); /* Use custom image */
    background-size: cover;
    animation: fly2 2s linear forwards;
    animation-delay: 0s;
  }

  .flying-dart3 {
    position: relative;
    width: 60px; /* Adjust width and height as needed */
    height: 40px;
    background-image: url('../assets/images/dart-illustration.png'); /* Use custom image */
    background-size: cover;
    animation: fly3 2s linear forwards;
    animation-delay: 0s;
  }

  .Board {
    width: 500px; /* Adjust width and height as needed */
    height: 500px;
    position: relative;
    z-index: -1;
    top: -200px; /* Adjust top position as needed */
    left: -800px;
  }

  .fadeText {
    font-size: 200px;
    color: #FFD700;
    animation: fadeIn 2s;
    position: absolute;
    left: 690px; /* Move the h1 50 pixels to the right */
    top: 333px; /* Move the h1 20 pixels down */
}
</style>
