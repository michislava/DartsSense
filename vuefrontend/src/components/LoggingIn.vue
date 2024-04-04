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
im

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

<style scoped>
.wrap {
    border: 4px solid #615a73;
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    padding: 50px;
    padding-top: 20px;
    align-items: center ;
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
    border: 2px solid #615a73;
    border-radius: 5px;
    width: 100%;
}

.form_field:focus {
    border: #4cf889;
}

.field_title {
    color: #c6caed;
}

</style>