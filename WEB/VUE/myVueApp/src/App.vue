<script>
// 声明式渲染，可以提高开发效率
export default {
  data() {
    return {
      number : 0,
      name : "xaiowang"
    }
  }
}
</script>

<template>
  <div>
    {{number}}
    {{name}}
  </div>
</template>

<style scoped>
</style>
