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
        <video
          v-if="pellicula.video"
          class="w-full h-auto"
          :src="`/video/${pellicula.video}#t=0.1`"
          muted
          preload="metadata"
        ></video>
        <img
          v-else-if="pellicula.imago"
          class="w-full h-auto transition-transform duration-200 hover:scale-105"
          :src="`/imagines/pellicula/${pellicula.imago}`"
          :alt="pellicula.titulo"
        />
      </div>
      <p class="text-white text-sm italic mt-1">{{ pellicula.titulo }} </p>
    </RouterLink>
  </div>
</template>


<style scoped>

</style>
