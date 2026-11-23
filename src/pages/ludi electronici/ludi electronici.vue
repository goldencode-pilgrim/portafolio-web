<script setup lang="ts">
import Carrousel from '@/components/ui/carrousel/Carrousel.vue';
import { ludi } from '@/lib/dataludi';

// Las imágenes que muestra el carrusel salen de dataludi.ts…
const imaginum = ludi.map(l => l.imago);

// …y cada imagen enlaza a la ruta de su juego según dataludi.ts
// (los juegos sin `ruta` definida enlazan a '/')
const enlaces = Object.fromEntries(
  ludi.map(l => [l.imago, l.ruta ?? '/']),
);
</script>


<template>
  <!-- Fondo de un solo color y sin scroll: h-full + overflow-hidden -->
  <div class="h-full w-full overflow-hidden bg-violet-950 text-white font-sans flex flex-col items-center justify-center gap-6 p-6 text-center">
    <h1 class="text-3xl font-bold">Ludi Electronici</h1>

    <!-- Imágenes dinámicas de dataludi.ts; cada una enlaza a su id.
         Una imagen sin entrada en los datos no navega ("si no, no") -->
    <Carrousel
      basePath="/imagines/videojuegos"
      :photos="imaginum"
      :enlaces="enlaces"
      :columnas="1"
      :autoplay-delay="3000"
    />
  </div>
</template>


<style scoped>

</style>
