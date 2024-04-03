<template>
    <header>
        <div class="sidebar" :style="{width : sbw}">
            <span
                class="collapse-icon"
                @click="toggleSidebar">
                <i class="fas fa-angle-double-left" ></i>
            </span>
            <RouterLink to="/">Home</RouterLink>
            <RouterLink to="/about">About</RouterLink>
            <RouterLink to="/register">Register</RouterLink>
        </div>
    </header>
    <RouterView />
</template>

<script>
import { RouterLink, RouterView } from 'vue-router'
import { collapsed, toggleSidebar, sbw} from './state.js'

export default {
    name: 'Navbar',
    components: {
        RouterLink,
        RouterView,

    },
    setup() {
        return { collapsed, toggleSidebar, sbw}
    },
}
</script>

<style>
:root {
    --sb-bg-color: #2f855a;
    --sb-it-hover: green;
    --sb-item-active: #276567;
}
</style>

<style scoped>
.sidebar {
    color: white;
    background-color: var(--sb-bg-color);
    float: left;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    bottom: 0;
    padding: 0.5em;

    transition: 0.3s ease;

    display: flex;
    flex-direction: column;
}

.collapse-icon {
  position: absolute;
  bottom: 0;
  padding: 0.75em;

  color: rgba(255, 255, 255, 0.7);

  transition: 0.2s linear;
}

.rotate-180 {
  transform: rotate(180deg);
  transition: 0.2s linear;
}

</style>