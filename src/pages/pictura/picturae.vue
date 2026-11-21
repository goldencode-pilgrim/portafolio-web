<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { picturae } from '@/lib/picturae';

const route = useRoute();

const cuadro = computed(() =>
  picturae.find((p) => p.id === Number(route.params.id)),
);
</script>


<template>
  <div class="bg-purple-900 min-h-full w-full text-white font-sans text-center flex flex-col items-center gap-4 p-6">
    <template v-if="cuadro">
      <img
        class="w-full max-w-xl aspect-square object-cover rounded-md border border-black"
        :src="`/imagines/pictura/${cuadro.imago}`"
        :alt="cuadro.titulo"
      />
      <h1 class="text-2xl font-bold">{{ cuadro.titulo }}</h1>
      <p class="text-sm opacity-75">id: {{ cuadro.id }}</p>
    </template>

    <template v-else>
      <h1 class="text-2xl font-bold">Cuadro no encontrado</h1>
      <p>No existe ningún cuadro con id: {{ route.params.id }}</p>
    </template>

    <RouterLink :to="{ name: 'pinacotheca' }" class="underline">← Volver a la galería</RouterLink>
  </div>
</template>


<style scoped>

</style>
