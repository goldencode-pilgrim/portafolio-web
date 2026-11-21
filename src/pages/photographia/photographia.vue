<script setup lang="ts">
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import { photographiae } from '@/lib/photographiae';

const route = useRoute();

const photographia = computed(() =>
  photographiae.find((p) => p.id === Number(route.params.id)),
);
</script>


<template>
  <div class="bg-pink-900 min-h-full w-full text-white font-sans text-center flex flex-col items-center gap-4 p-6">
    <template v-if="photographia">
      <img
        class="w-full max-w-xl aspect-square object-cover rounded-md border border-black"
        :src="`/imagines/photographia/${photographia.imago}`"
        :alt="photographia.titulo"
      />
      <h1 class="text-2xl font-bold">{{ photographia.titulo }}</h1>
      <p class="text-sm opacity-75">id: {{ photographia.id }}</p>
    </template>

    <template v-else>
      <h1 class="text-2xl font-bold">Fotografía no encontrada</h1>
      <p>No existe ninguna fotografía con id: {{ route.params.id }}</p>
    </template>

    <RouterLink :to="{ name: 'pinacotheca-photo' }" class="underline">← Volver a la pinacotheca</RouterLink>
  </div>
</template>


<style scoped>

</style>
