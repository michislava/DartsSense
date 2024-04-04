<template>
    <div class="wrap">
        <h3 class="form_title">Log In</h3>
        <form @submit="handleSubmit">
            <div>
                <label class="field_title">Username</label>
                <div>
                    <input class="form_field" type="text" v-model="username" placeholder="Username"/>
                </div>
            </div>
            <div>
                <label class="field_title">Password</label>
                <div>
                    <input class="form_field" type="password" v-model="pass" placeholder="Password"/>
                </div>
            </div>
            <div>
                <Button text="Log In"></Button>
            </div>  
        </form>
        
    </div>

</template>

<script>

import Button from './Button.vue';
import axios from 'axios'; 
import "../assets/style.css"

export default {
    name: 'Registration',
    components: {
        Button
    },
    data() {
        return {
            username: '',
            pass: ''
        }
    },
    methods: {
        async handleSubmit(e) {
            e.preventDefault();
            try {
                const response = await axios.post('/api/login', {
                    data: JSON.stringify({
                    username: this.username,
                    password: this.pass
                }),
                headers: {
                    'Content-Type': 'application/json' // Set content type to JSON
                }
            });
                console.log('Login successful:', response.data);
                // Redirect or perform actions after successful login
            } catch (error) {
                console.error('Error logging in:', error);
                // Handle error, such as displaying an error message to the user
            }
        }
    }
}

</script>
