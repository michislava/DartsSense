<template>
    <div>{{ answer }}</div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "Axios",
    data() {
      return {
        answer: {},
      };
    },
    methods: {
      async getAnswer() {
        const { data } = await axios.get("https://yesno.wtf/api");
        this.answer = data;
      },
    },
    beforeMount() {
      this.getAnswer();
    },
  };
  </script>