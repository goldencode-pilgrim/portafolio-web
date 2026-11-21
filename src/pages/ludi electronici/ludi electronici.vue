<script setup lang="ts">
import Carrousel from '@/components/ui/carrousel/Carrousel.vue';

// Demo: única imagen que existe ahora. Sustituye por las capturas del juego
// (crea public/imagines/ludici/ y cambia basePath + photos).
const imaginum = ['autoretratoartista2023', 'autoretratoartista2023', 'autoretratoartista2023'];
</script>


<template>
  <!-- Fondo de un solo color y sin scroll: h-full + overflow-hidden -->
  <div class="h-full w-full overflow-hidden bg-violet-950 text-white font-sans flex flex-col items-center justify-center gap-6 p-6 text-center">
    <h1 class="text-3xl font-bold">Ludi Electronici</h1>

    <Carrousel basePath="/imagines/pictura" :photos="imaginum" :autoplay-delay="3000" />
  </div>
</template>


<style scoped>

</style>
