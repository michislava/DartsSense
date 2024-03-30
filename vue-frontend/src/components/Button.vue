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
    }
}
</script>

<style scoped>
.btn {
    background-color: #c5fcd8;
    border: 2px solid #4cf889;
    border-radius: 6px;
    width: 100%;
    font-size: 16px;
    top: 5px;
    font-weight: 10;
    margin-top: 8px;
}
</style>