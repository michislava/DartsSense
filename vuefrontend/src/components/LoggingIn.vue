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
            const data = {
                username: this.username,
                pass: this.pass,
            };
            try {

                const response = await axios.post('http://34.88.180.160:9000/аpi/login', data, {
                    headers: {
                        'Content-Type': 'application/json' // Set content type to JSON
                    }
                });
                
                console.log('User logged in successfully:', response.parsedData);
                // Optionally, perform actions after successful registration
            } catch (error) {
                console.error('Error loggin in user:', error);
                // Optionally, handle registration error
            }
        }
    }
}

</script>
