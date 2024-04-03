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
                    <input class="form_field" type="text" v-model="deviceid" placeholder="Device-ID"/>
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
            deviceid: '',
            skill: '',
        }
    },
    methods: {
        handleSubmit(e) {
            e.preventDefault();
            const data = {
                firstname: this.firstname,
                lastname: this.lastname,
                username: this.username,
                email: this.email,
                pass: this.pass,
                deviceid: this.deviceid,
                skill: this.skill
            }
            console.log(data);
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