<script setup lang="ts">

</script>

<template>
  <!-- Layaout propio de la sección Sunroja & Lunablack, mismo esquema que Layaoutludici -->
  <div class="grid grid-rows-[auto_1fr_auto] min-h-full bg-neutral-900 text-white">
    <header class="bg-neutral-900 w-full border-b border-black">
      <div class="flex flex-col md:flex-row justify-between items-center p-3 mx-auto max-w-5xl md:px-20 gap-2">
        <h1 class="font-bold text-lg tracking-wide">Sunroja &amp; Lunablack</h1>

        <div class="flex items-center gap-6">
          <RouterLink
            to="/ludielectronici/2"
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

    <footer class="bg-neutral-900 text-center py-6 w-full border-t border-black">
      <div>
        <strong>Sunroja &amp; Lunablack</strong>
      </div>
      <small class="opacity-75">Portafolio · Apps y arte multimedia</small>
    </footer>
  </div>
</template>


<style scoped>

</style>
