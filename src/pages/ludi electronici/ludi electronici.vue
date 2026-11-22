<script setup lang="ts">
import Carrousel from '@/components/ui/carrousel/Carrousel.vue';

// Demo: única imagen que existe ahora. Sustituye por las capturas del juego
// (crea public/imagines/ludici/ y cambia basePath + photos). Con 4 fotos la
// tira queda completa; el componente repite la lista si hay menos.
const imaginum = ['autoretratoartista2023', 'autoretratoartista2023', 'autoretratoartista2023', 'autoretratoartista2023'];
</script>


<template>
  <!-- Fondo de un solo color y sin scroll: h-full + overflow-hidden -->
  <div class="h-full w-full overflow-hidden bg-violet-950 text-white font-sans flex flex-col items-center justify-center gap-6 p-6 text-center">
    <h1 class="text-3xl font-bold">Ludi Electronici</h1>

    <Carrousel basePath="/imagines/pictura" :photos="imaginum" :autoplay-delay="3000">
      <!-- Capa superpuesta por columna (demo): cada div con `absolute inset-0`
           que pongas aquí cubrirá su columna. Borra este cuando añadas los tuyos -->
      <template #columne>
        <div class="absolute inset-0 bg-violet-900/0 group-hover:bg-violet-900/40 transition-colors pointer-events-none"></div>
      </template>
    </Carrousel>
  </div>
</template>


<style scoped>

</style>
