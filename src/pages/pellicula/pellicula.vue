<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { pelliculae } from '@/lib/pelliculae';

const route = useRoute();

const pellicula = computed(() =>
  pelliculae.find((p) => p.id === Number(route.params.id)),
);
</script>


<template>
  <div class="bg-pink-300 min-h-full w-full text-black font-sans text-center flex flex-col items-center gap-4 p-6">
    <template v-if="pellicula">
      <img
        class="w-full max-w-xl aspect-square object-cover rounded-md border border-black"
        :src="`/imagines/pellicula/${pellicula.imago}`"
        :alt="pellicula.titulo"
      />
      <h1 class="text-2xl font-bold">{{ pellicula.titulo }}</h1>
      <p class="text-sm opacity-75">id: {{ pellicula.id }}</p>
    </template>

    <template v-else>
      <h1 class="text-2xl font-bold">Película no encontrada</h1>
      <p>No existe ninguna película con id: {{ route.params.id }}</p>
    </template>

    <RouterLink :to="{ name: 'pinacotheca-pelicula' }" class="underline">← Volver a las películas</RouterLink>
  </div>
</template>


<style scoped>

</style>
