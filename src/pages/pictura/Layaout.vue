<script setup lang="ts">

</script>

<template>
    <div class="flex h-screen">
      <nav class="w-20 bg-indigo-900 text-white flex flex-col items-center gap-2.5 p-2">
        <h1>Menú</h1>
      </nav>
      <main class="flex-1 overflow-y-auto">
        <RouterView />
      </main>
    </div>
</template>


<style scoped>

</style>