<script setup lang="ts">
import Carrousel from '@/components/ui/carrousel/Carrousel.vue';

// Miniaturas reales en public/imagines/videojuegos/ (con extensión .png)
const imaginum = ['F&D-DANA-diariodesarrollo1-miniatura.png', 'Polcompass.png', 'portadasunrojavue.png'];
</script>


<template>
  <!-- Fondo de un solo color y sin scroll: h-full + overflow-hidden -->
  <div class="h-full w-full overflow-hidden bg-violet-950 text-white font-sans flex flex-col items-center justify-center gap-6 p-6 text-center">
    <h1 class="text-3xl font-bold">Ludi Electronici</h1>

    <!-- Solo la celda que muestra la miniatura de F&D-DANA es enlace;
         las demás no navegan -->
    <Carrousel
      basePath="/imagines/videojuegos"
      :photos="imaginum"
      :autoplay-delay="3000"
      foto-enlazada="F&D-DANA-diariodesarrollo1-miniatura.png"
      ruta="/ludielectronici/f&d-dana/informatio"
    />
  </div>
</template>


<style scoped>

</style>
