<template>
    <div class="wrap">
        <form class="form" @submit="handleSubmit">
            <h3 class="form_title">Sign Up</h3>

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
                <label class="field_title">Skill-Level</label>
                <div>
                    <select class="form_field" name="sl" v-model="skill">
                        <option value="Beginner">Beginner</option>
                        <option value="Intermediate">Intermediate</option>
                        <option value="Advanced">Advanced</option>
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
            skill: ''
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
                skill: this.skill
            }
            console.log(data);
        }
    }
}
</script>

<style scoped>
.wrap {
    border: 2px solid green;
    border-radius: 8px;
    padding: 50px;
    padding-top: 20px;
    align-items: center ;
}
.form_title {
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
    border: 2px solid #c5fcd8;
    border-radius: 5px;
    width: 100%;
    
}
.form_field:focus {
    border: #4cf889;
}
</style>