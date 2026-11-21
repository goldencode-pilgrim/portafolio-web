<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue';

// Carrusel sin dependencias externas (el portafolio no tiene embla-carousel).
// Misma interfaz que CarrusImaginum.vue de vue-web, adaptada.
interface Props {
  /** Nombres de archivo SIN extensión */
  photos: string[];
  /** Carpeta en /public, ej: /imagines/ludici */
  basePath: string;
  /** Milisegundos entre imágenes; 0 desactiva el autoplay */
  autoplayDelay?: number;
}

const props = withDefaults(defineProps<Props>(), {
  autoplayDelay: 3000,
});

const index = ref(0);

const next = () => {
  index.value = (index.value + 1) % props.photos.length;
};

const prev = () => {
  index.value = (index.value - 1 + props.photos.length) % props.photos.length;
};

let timer: number | undefined;

onMounted(() => {
  if (props.autoplayDelay > 0) {
    timer = window.setInterval(next, props.autoplayDelay);
  }
});

onUnmounted(() => {
  if (timer) window.clearInterval(timer);
});
</script>


<template>
  <div class="relative w-full max-w-md md:max-w-xl flex flex-col items-center gap-4 select-none">
    <img
      class="w-full max-h-[55vh] object-contain rounded-md border border-black bg-violet-800 shadow-lg"
      :src="`${props.basePath}/${props.photos[index]}.jpg`"
      :alt="`Imagen ${index + 1} del carrusel`"
    />

    <div class="flex items-center gap-4">
      <button
        @click="prev"
        class="w-10 h-10 rounded-md bg-violet-600 hover:bg-violet-500 text-white font-bold transition-colors"
        aria-label="Anterior"
      >‹</button>
      <p class="text-sm opacity-80">{{ index + 1 }} / {{ props.photos.length }}</p>
      <button
        @click="next"
        class="w-10 h-10 rounded-md bg-violet-600 hover:bg-violet-500 text-white font-bold transition-colors"
        aria-label="Siguiente"
      >›</button>
    </div>
  </div>
</template>


<style scoped>

</style>
