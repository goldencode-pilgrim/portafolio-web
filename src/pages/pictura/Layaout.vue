<script setup lang="ts">
import { House } from '@lucide/vue';
import Button from '@/components/ui/button/Button.vue';

interface Sectio {
  nomen: string;
  ruta: string;
}

const sectiones: Sectio[] = [
  { nomen: 'Artes gráficas', ruta: '/pingo/imagines' },
  { nomen: 'Artes pictóricas', ruta: '/pictura/pinacotheca' },
  { nomen: 'Artes fotográficas', ruta: '/photographia/pinacotheca' },
  { nomen: 'Artes audiovisuales', ruta: '/pelicula/pinacotheca' },
  { nomen: 'Artes interactivas', ruta: '/ludielectronici/collectione' },
  { nomen: 'MAICI', ruta: '/maici' },
  { nomen: 'RR.SS', ruta: '/rrss' },
];
</script>

<template>
    <div class="flex h-screen">
      <nav class="w-48 shrink-0 bg-indigo-900 border-4 border-black text-white flex flex-col items-stretch gap-2.5 p-2 overflow-y-auto">
        <RouterLink
          to="/"
          title="Domus"
          aria-label="Domus (inicio)"
          class="self-center flex items-center justify-center size-12 rounded-md bg-black hover:bg-indigo-700 transition-colors"
        >
          <House class="size-6" />
        </RouterLink>

        <!-- Un botón por sección: as-child hace que el RouterLink herede
             los estilos del Button sin anidar <button> dentro de <a> -->
        <Button
          v-for="sectio in sectiones"
          :key="sectio.ruta"
          as-child
          variant="domus"
          class="text-sm px-3 py-2"
        >
          <RouterLink :to="sectio.ruta">{{ sectio.nomen }}</RouterLink>
        </Button>
      </nav>
      <main class="flex-1 overflow-y-auto">
        <RouterView />
      </main>
    </div>
</template>


<style scoped>

</style>
