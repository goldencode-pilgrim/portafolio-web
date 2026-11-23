<script setup lang="ts">

</script>

<template>
  <!-- Layaout propio de la sección Polcompball, mismo esquema que Layaoutludici -->
  <div class="grid grid-rows-[auto_1fr_auto] min-h-full bg-red-950 text-white">
    <header class="bg-red-950 w-full border-b border-black">
      <div class="flex flex-col md:flex-row justify-between items-center p-3 mx-auto max-w-5xl md:px-20 gap-2">
        <h1 class="font-bold text-lg tracking-wide">Polcompball</h1>

        <div class="flex items-center gap-6">
          <RouterLink
            to="/ludielectronici/1"
            active-class="font-bold underline"
          >
            Informatio
          </RouterLink>
          <RouterLink
            to="/ludielectronici/collectione"
            class="px-4 py-1.5 rounded-md bg-red-700 hover:bg-red-600 transition-colors"
          >
            Exit
          </RouterLink>
        </div>
      </div>
    </header>

    <main class="w-full">
      <RouterView />
    </main>

    <footer class="bg-red-950 text-center py-6 w-full border-t border-black">
      <div>
        <strong>Polcompball</strong>
      </div>
      <small class="opacity-75">Portafolio · Apps y arte multimedia</small>
    </footer>
  </div>
</template>


<style scoped>

</style>
