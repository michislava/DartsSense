import {ref, computed} from 'vue'

export const collapsed = ref(false)
export const toggleSidebar = () => (collapsed.value = !collapsed.value)

export const SIDEBAR_W = 180
export const SIDEBAR_W_COLLAPSED = 38
export const sbw = computed(
    () => `${collapsed.value ? SIDEBAR_W_COLLAPSED : SIDEBAR_W}px`
)