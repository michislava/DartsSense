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

<style scoped>
.wrap {
    border: 4px solid #615a73;
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    padding: 50px;
    padding-top: 20px;
    align-items: center ;
    font-family: 'Courier New', Courier, monospace;
}
.form_title {
    color: #c6caed;
    font-weight: bold;
    align-items: left;
    align-content: left;
    text-align: center;
    padding-bottom: 20px;
}

.from {
    position: center;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);

}
.form_field {
    font: optional;
    border: 2px solid #79708f;
    border-radius: 5px;
    width: 100%;
    transition: ease;
    transition-duration: 0.5s;
    margin-bottom: 5px;
}

.form_field:focus {
    border: #615a73;
    transition: ease;
    transition-duration: 0.5s;
    border-radius: 20px;
}

.field_title {
    color: #c6caed;
}

.dropdown {
    font: optional;
    border: 2px solid #79708f;
    border-radius: 5px;
    width: 100%;
    transition: all .5s ease;
    margin-bottom: 5px;
}

.dropdown:hover {
    font: optional;
}

.dropdown:focus { /* Update focus styling */
    transition: ease;
    transition-duration: 0.5s;
    margin-bottom: 50px;
}

.dropdown .option {
    font-size: 13px;
    color: #888;
    cursor: pointer;
    transition: all .3s ease-in-out;
    float: right;
    line-height: 20px;
}

</style>