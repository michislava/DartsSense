<template>
    <div class="wrap">
        <form class="form" @submit="handleSubmit">
            <h1 class="form_title">Sign Up</h1>

            <div>
                <label class="field_title">First Name</label>
                <div class="form">
                    <input class="form_field" type="text" v-model="firstname" placeholder="First Name"/>
                </div>
            </div>
            <div>
                <label class="field_title">Last Name</label>
                <div>
                    <input class="form_field" type="text" v-model="lastname" placeholder="Last Name"/>
                </div>
            </div>
            <div>
                <label class="field_title">Username</label>
                <div>
                    <input class="form_field" type="text" v-model="username" placeholder="Username"/>
                </div>
            </div>
            <div>
                <label class="field_title">E-Mail</label>
                <div>
                    <input class="form_field" type="email" v-model="email" placeholder="E-Mail"/>
                </div>
            </div>
            <div>
                <label class="field_title">Password</label>
                <div>
                    <input class="form_field" type="password" v-model="pass" placeholder="Password"/>
                </div>
            </div>
            <div>
                <label class="field_title">Device-ID</label>
                <div>
                    <input class="form_field" type="text" v-model="deviceId" placeholder="Device-ID"/>
                </div>
            </div>
            <div>
                <label id="select" class="field_title">Skill-Level</label>
                <div>
                    <select class="dropdown" name="sl" v-model="skill" placeholder="Skill-Level" 
                    @mouseenter="$event.target.blur()">
                        <option class="option" value="Beginner">Beginner</option>
                        <option class="option" value="Intermediate">Intermediate</option>
                        <option class="option" value="Advanced">Advanced</option>
                    </select>
                </div>
            </div>
            <div>
                <Button text="Sign-Up"></Button>
            </div>  
        </form>
        
    </div>

</template>

<script>
import Button from './Button.vue';
import axios from "axios";
import "../assets/style.css"

export default {
    name: 'Registration',
    components: {
        Button
    },
    data() {
        return {
            firstname: '',
            lastname: '',
            username: '',
            email: '',
            pass: '',
            deviceId: '',
            skill: '',
        }
    },
    methods: {
        async handleSubmit(e) {
            e.preventDefault();
            const data = {
                firstname: this.firstname,
                lastname: this.lastname,
                username: this.username,
                email: this.email,
                pass: this.pass,
                deviceId: this.deviceId,
                skill: this.skill
            };
            try {

                const response = await axios.post('http://127.0.0.1:9000/api/register', data, {
                    headers: {
                        'Content-Type': 'application/json' // Set content type to JSON
                    }
                });
                
                console.log('User registered successfully:', response.parsedData);
                // Optionally, perform actions after successful registration
            } catch (error) {
                console.error('Error registering user:', error);
                // Optionally, handle registration error
            }
        },
    }
}
</script>   