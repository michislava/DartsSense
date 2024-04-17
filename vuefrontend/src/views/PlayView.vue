<template>
    <div class="wrap">
        <h1 class="form_title">Play</h1>
        <Button class="beton" @click="submit" text="Create New Game"></Button>
        <div id="2" class="wrap">
            <h1 class="form_title">Previous Games</h1>
            
        </div>   
    </div>
</template>
  
<script>
import Button from "../components/Button.vue"
import "../assets/style.css"

export default {
    name: 'Play',
    components: {
        Button
    },
    methods: {
        submit() {
            this.$router.push('/create-game');
        }
    }
}
</script>

<style scoped>
.beton {
    padding-bottom: 20px;
}
</style>

