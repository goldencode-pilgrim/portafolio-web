<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { ludi } from '@/lib/dataludi';

const route = useRoute();

const ludus = computed(() =>
  ludi.find(l => l.id === Number(route.params.id)),
);
</script>


<template>
  <!-- Ficha de un videojuego, según la id de la URL -->
  <div class="bg-violet-950 min-h-full w-full text-white font-sans text-center flex flex-col items-center gap-4 p-6">
    <template v-if="ludus">
      <img
        class="max-h-[60vh] w-auto max-w-full object-contain rounded-md border border-black"
        :src="`/imagines/videojuegos/${ludus.imago}`"
        :alt="ludus.nomen"
      />
      <h1 class="text-2xl font-bold">{{ ludus.nomen }}</h1>
      <p class="text-sm opacity-75">id: {{ ludus.id }}</p>
      <p v-if="ludus.descriptio" class="max-w-2xl">{{ ludus.descriptio }}</p>
    </template>

    <template v-else>
      <h1 class="text-2xl font-bold">Juego no encontrado</h1>
      <p>No existe ningún juego con id: {{ route.params.id }}</p>
    </template>

    <RouterLink :to="{ name: 'collectione' }" class="underline">← Volver a Ludi Electronici</RouterLink>
  </div>
</template>


<style scoped>

</style>
