<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref } from 'vue';

// Carrusel en tira horizontal: 4 columnas × 1 fila, hueco proporcional
// y una ranura (#columne) para superponer un div sobre cada columna.
interface Props {
  /** Nombres de archivo, con o sin extensión */
  photos: string[];
  /** Carpeta en /public, ej: /imagines/videojuegos */
  basePath: string;
  /** Milisegundos entre desplazamientos; 0 desactiva el autoplay */
  autoplayDelay?: number;
  /** Si una celda muestra ESTA imagen, se convierte en enlace */
  fotoEnlazada?: string;
  /** Destino del enlace cuando la celda muestra fotoEnlazada */
  ruta?: string;
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

// Las 4 imágenes visibles: se repite la lista hasta llenar las columnas
// y se desplaza según el índice (efecto cinta de carrusel).
const visibles = computed(() => {
  const total = props.photos.length;
  if (total === 0) return [];
  const base: string[] = [];
  while (base.length < 4) base.push(...props.photos);
  const start = index.value % total;
  return [...base.slice(start), ...base.slice(0, start)].slice(0, 4);
});

// ¿Esta celda se convierte en enlace? Solo si hay fotoEnlazada + ruta
// y la imagen mostrada coincide con fotoEnlazada.
const esEnlace = (photo: string) =>
  !!props.fotoEnlazada && !!props.ruta && photo === props.fotoEnlazada;

// URL de la imagen: acepta nombres con o sin extensión
const urlDe = (photo: string) =>
  photo.includes('.') ? `${props.basePath}/${photo}` : `${props.basePath}/${photo}.jpg`;

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
  <div class="w-full max-w-4xl mx-auto flex flex-col items-center gap-4 select-none">
    <!-- Tira horizontal: 4 columnas × 1 fila, hueco proporcional -->
    <div class="w-full grid grid-cols-4 grid-rows-1 gap-4">
      <div
        v-for="(photo, i) in visibles"
        :key="`${photo}-${i}`"
        class="group relative overflow-hidden rounded-md border border-black"
      >
        <!-- Si muestra la imagen enlazada → RouterLink; si no → imagen sin enlace -->
        <RouterLink
          v-if="esEnlace(photo)"
          :to="props.ruta!"
          class="block h-full w-full"
        >
          <img
            class="aspect-[3/4] w-full object-cover transition-transform duration-300 group-hover:scale-105"
            :src="urlDe(photo)"
            :alt="`Imagen ${i + 1} del carrusel`"
          />
        </RouterLink>
        <img
          v-else
          class="aspect-[3/4] w-full object-cover transition-transform duration-300 group-hover:scale-105"
          :src="urlDe(photo)"
          :alt="`Imagen ${i + 1} del carrusel`"
        />

        <!-- Ranura: aquí el padre puede superponer un div sobre esta columna -->
        <slot name="columne" :index="i" :photo="photo" />
      </div>
    </div>

    <!-- Controles -->
    <div class="flex items-center gap-4">
      <button
        @click="prev"
        class="w-10 h-10 rounded-md bg-violet-600 hover:bg-violet-500 text-white font-bold transition-colors"
        aria-label="Anterior"
      >‹</button>
      <p class="text-sm opacity-80">{{ (index % props.photos.length) + 1 }} / {{ props.photos.length }}</p>
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
