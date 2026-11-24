<script setup lang="ts">
import { delineationes } from '@/lib/delineationes';
</script>


<template>
  <div class="bg-gray-300 min-h-full w-full font-sans text-center p-6 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
    <RouterLink
      v-for="delineatio in delineationes"
      :key="delineatio.id"
      :to="{ name: 'delineationes', params: { id: delineatio.id } }"
      class="block"
    >
      <div class="overflow-hidden rounded-t-md border border-black">
        <img
          class="w-full h-auto transition-transform duration-200 hover:scale-105"
          :src="`/imagines/delineationes/${delineatio.imago}`"
          :alt="delineatio.titulo"
        />
      </div>
      <p class="text-black text-sm italic mt-1">{{ delineatio.titulo }} </p>
    </RouterLink>
  </div>
</template>


<style scoped>

</style>
