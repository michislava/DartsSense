<template>
    <div class="wrap">
        <form class="form" @submit="handleSubmit">
            <h1 class="form_title">Create a Game</h1>

            <div>
                <label class="field_title">Game Name</label>
                <div class="form">
                    <input class="form_field" type="text" v-model="gamename" placeholder="Game Name"/>
                </div>
            </div>
            <div>
                <label class="field_title">Player 1</label>
                <div>
                    <input class="form_field" type="text" v-model="user1" placeholder="Player 1"/>
                </div>
            </div>
            <div>
                <label class="field_title">Player 2</label>
                <div>
                    <input class="form_field" type="text" v-model="user2" placeholder="Player 2"/>
                </div>
            </div>
            <div>
                <Button text="Create Game"></Button>
            </div>  
        </form>
        
    </div>

</template>

<script>
import Button from './Button.vue';
import axios from "axios";
import "../assets/style.css"

export default {
    name: 'GameCreation',
    components: {
        Button
    },
    data() {
        return {
            gamename: '',
            user1: '',
            user2: '',
        }
    },
    methods: {
        async handleSubmit(e) {
            e.preventDefault();
            const data = {
                gamename: this.gamename,
                user1: this.user1,
                user2: this.user2
            };
            try {
                const response = await axios.post('http://backend:9000/create-game', data);
               // Optionally, perform actions after successful registration
            } catch (error) {
                // Optionally, handle registration error
                console.log("err");
            }
        },
    }
}
</script>
