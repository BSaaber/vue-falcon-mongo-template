<script setup>
import LayoutDefault from '~/layout/default.vue'
import { computed, ref } from 'vue'
import { useRoute } from 'vue-router'

const layouts = {
  default: LayoutDefault,
}

const data = ref(null)

const getTest = async () => {
  const url = 'http://localhost:3000/handler'
  const res = await fetch(url)
  data.value = res
}

getTest()

const route = useRoute()
const computedLayout = computed(() => {
  return layouts[route.meta.layout || 'default']
})
</script>

<template>
  DDDAAATTAAA {{ data  }}
  <component :is="computedLayout">
    <router-view />
  </component>
</template>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
