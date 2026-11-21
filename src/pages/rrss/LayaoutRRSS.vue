<script setup lang="ts">

</script>

<template>
  <div class="min-h-screen flex flex-col">
    <!-- Header con color propio sólido: el fondo de la página nunca lo tapa -->
    <header class="sticky top-0 z-20 bg-black text-white border-b border-white/20">
      <div class="max-w-3xl mx-auto flex items-center justify-between px-4 py-3">
        <h1 class="font-bold">RRSS</h1>
        <RouterLink to="/" class="text-sm hover:underline">← Portafolio</RouterLink>
      </div>
    </header>

    <main class="flex-1">
      <RouterView />
    </main>

    <footer class="bg-black text-white text-center py-6 border-t border-white/20">
      <div>
        <strong>Golden the pilgrim</strong> — Redes y ensayos
      </div>
      <small class="opacity-75">Portafolio · Apps y arte multimedia</small>
    </footer>
  </div>
</template>


<style scoped>

</style>
