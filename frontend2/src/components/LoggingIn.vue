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
        handleSubmit(e) {
            e.preventDefault();
            const data = {
                username: this.username,
                pass: this.pass
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