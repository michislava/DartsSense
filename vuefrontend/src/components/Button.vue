<template>
    <div>
        <button class="btn">{{text}}</button>
    </div>
</template>

<script>
export default {
    name: 'Button',
    props: {
        text: String,
    },
}
</script>

<style scoped>
.btn {
    background-color: #8e839b;
    border: 2px solid #615a73;
    border-radius: 6px;
    width: 100%;
    font-size: 16px;
    top: 5px;
    font-weight: bold;
    margin-top: 8px;
    color: rgb(226, 226, 226);
    transition-duration: 0.5s;
    margin-top: 10px;

}

.btn:hover {
    background-color: #615a73;
    transition-duration: 0.5s;
    border-radius: 20px;
}
</style>