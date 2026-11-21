<script setup lang="ts">

</script>

<template>
  <!-- Layaout propio de la sección fidesetdesperatioDANA,
       similar al Layaout.vue de Simpsons (vue-web) pero adaptado:
       fondo violeta, logo textual y enlaces propios. -->
  <div class="grid grid-rows-[auto_1fr_auto] min-h-full bg-violet-900 text-white">
    <header class="bg-violet-900 w-full border-b border-black">
      <div class="flex flex-col md:flex-row justify-between items-center p-3 mx-auto max-w-5xl md:px-20 gap-2">
        <h1 class="font-bold text-lg tracking-wide">Fides et Desperatio DANA</h1>

        <div class="flex items-center gap-6">
          <RouterLink
            to="/ludielectronici/f&d-dana/informatio"
            active-class="font-bold underline"
          >
            Informatio
          </RouterLink>
          <RouterLink
            to="/ludielectronici/f&d-dana/personae"
            active-class="font-bold underline"
          >
            Personae
          </RouterLink>
          <RouterLink
            to="/ludielectronici/collectione"
            class="px-4 py-1.5 rounded-md bg-violet-600 hover:bg-violet-500 transition-colors"
          >
            Exit
          </RouterLink>
        </div>
      </div>
    </header>

    <main class="w-full">
      <RouterView />
    </main>

    <footer class="bg-violet-900 text-center py-6 w-full border-t border-black">
      <div>
        <strong>Fides et Desperatio</strong> — DANA
      </div>
      <small class="opacity-75">Portafolio · Apps y arte multimedia</small>
    </footer>
  </div>
</template>


<style scoped>

</style>
