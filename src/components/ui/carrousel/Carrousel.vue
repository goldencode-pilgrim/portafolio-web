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
  /** Mapa imago → ruta: las celdas cuya imagen tenga entrada aquí son enlaces */
  enlaces?: Record<string, string>;
  /** Nº de imágenes visibles en la tira (1 = una sola imagen) */
  columnas?: number;
}

const props = withDefaults(defineProps<Props>(), {
  autoplayDelay: 3000,
  columnas: 4,
});

const index = ref(0);

const next = () => {
  index.value = (index.value + 1) % props.photos.length;
};

const prev = () => {
  index.value = (index.value - 1 + props.photos.length) % props.photos.length;
};

// Las imágenes visibles: se repite la lista hasta llenar las columnas
// y se desplaza según el índice (efecto cinta de carrusel).
const visibles = computed(() => {
  const total = props.photos.length;
  const cols = Math.max(1, props.columnas);
  if (total === 0) return [];
  const base: string[] = [];
  while (base.length < cols) base.push(...props.photos);
  const start = index.value % total;
  return [...base.slice(start), ...base.slice(0, start)].slice(0, cols);
});

// ¿Esta celda se convierte en enlace? Solo si su imagen tiene entrada
// en el mapa de enlaces.
const esEnlace = (photo: string) =>
  !!props.enlaces && !!props.enlaces[photo];

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
  <div
    class="mx-auto flex flex-col items-center gap-4 select-none"
    :class="props.columnas === 1 ? 'w-full max-w-md md:max-w-xl' : 'w-full max-w-4xl'"
  >
    <!-- Tira horizontal: columnas × 1 fila, hueco proporcional -->
    <div
      class="w-full grid grid-rows-1 gap-4"
      :style="{ gridTemplateColumns: `repeat(${props.columnas}, minmax(0, 1fr))` }"
    >
      <div
        v-for="(photo, i) in visibles"
        :key="`${photo}-${i}`"
        class="group relative overflow-hidden rounded-md border border-black"
        :class="props.columnas === 1 ? 'w-fit mx-auto' : 'w-full'"
      >
        <!-- Si muestra la imagen enlazada → RouterLink; si no → imagen sin enlace -->
        <RouterLink
          v-if="esEnlace(photo)"
          :to="props.enlaces![photo]!"
          class="block h-full w-full"
        >
          <img
            class="transition-transform duration-300 group-hover:scale-105"
            :class="props.columnas === 1 ? 'block max-h-[55vh] w-auto mx-auto object-contain' : 'aspect-[3/4] w-full object-cover'"
            :src="urlDe(photo)"
            :alt="`Imagen ${i + 1} del carrusel`"
          />
        </RouterLink>
        <img
          v-else
          class="transition-transform duration-300 group-hover:scale-105"
          :class="props.columnas === 1 ? 'block max-h-[55vh] w-auto mx-auto object-contain' : 'aspect-[3/4] w-full object-cover'"
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
