<script setup lang="ts">
import { pelliculae } from '@/lib/pelliculae';
</script>


<template>
  <div class="bg-gray-900 min-h-full w-full font-sans text-center p-6 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
    <RouterLink
      v-for="pellicula in pelliculae"
      :key="pellicula.id"
      :to="{ name: 'pelicula', params: { id: pellicula.id } }"
      class="block"
    >
      <div class="overflow-hidden rounded-t-md border border-black">
        <img
          class="w-full h-auto transition-transform duration-200 hover:scale-105"
          :src="`/imagines/pellicula/${pellicula.imago}`"
          :alt="pellicula.titulo"
        />
      </div>
      <p class="text-white text-sm mt-1">{{ pellicula.titulo }} (id: {{ pellicula.id }})</p>
    </RouterLink>
  </div>
</template>


<style scoped>

</style>
