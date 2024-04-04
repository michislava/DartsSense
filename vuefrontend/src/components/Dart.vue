<template>
    <div class="greetings">
      <div className="flying-dart1" :style="dartStyle"></div>
    </div>
  </template>

<script>
export default {
  props: {
    startX: {
      type: Number,
      required: true
    },
    startY: {
      type: Number,
      required: true
    },
    endX: {
      type: Number,
      required: true
    },
    endY: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      dartStyle: {
        position: 'absolute',
        width: '110px',
        height: '70px',
        transform: `translate(${this.startX}px, ${this.startY}px)`
      }
    }
  },
  mounted() {
    setTimeout(() => {
      this.flyDart();
    }, Math.random() * 2000);;
  },
  methods: {
    flyDart() {
      let start = this.startX;
      const speed = 40;
      const end = this.endX;
      const distance = end - start;
      const arcHeight = Math.abs(this.startY - this.endY) * 0.5; 

      const interval = setInterval(() => {
        if (start <= end) {
          clearInterval(interval);
        } else {
          const percentage = (start - this.startX) / distance;
          const height = -1 * arcHeight * Math.pow(percentage - 0.5, 2) + arcHeight; // Quadratic function for arc
          const rotation = percentage * 360; // Rotate the dart as it moves
          this.dartStyle.transform = `translate(${start}px, ${this.startY - height}px) rotate(${rotation}deg)`;
          start -= speed;
        }
      }, 50);
    }
  }
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

</style>
