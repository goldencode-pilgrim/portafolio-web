<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { delineationes } from '@/lib/delineationes';

const route = useRoute();

const delineatio = computed(() =>
  delineationes.find((d) => d.id === Number(route.params.id)),
);
</script>


<template>
  <div class="bg-gray-900 min-h-full w-full text-white font-sans text-center flex flex-col items-center gap-4 p-6">
    <template v-if="delineatio">
      <img
        class="w-full max-w-xl aspect-square object-cover rounded-md border border-black"
        :src="`/imagines/pingo/${delineatio.imago}`"
        :alt="delineatio.titulo"
      />
      <h1 class="text-2xl font-bold">{{ delineatio.titulo }}</h1>
      <p class="text-sm opacity-75">id: {{ delineatio.id }}</p>
    </template>

    <template v-else>
      <h1 class="text-2xl font-bold">Dibujo no encontrado</h1>
      <p>No existe ningún dibujo con id: {{ route.params.id }}</p>
    </template>

    <RouterLink :to="{ name: 'imagines' }" class="underline">← Volver a los dibujos</RouterLink>
  </div>
</template>


<style scoped>

</style>
