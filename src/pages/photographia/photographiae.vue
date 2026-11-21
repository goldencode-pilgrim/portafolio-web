<script setup lang="ts">
import { photographiae } from '@/lib/photographiae';
</script>


<template>
  <div class="bg-gray-300 min-h-full w-full font-sans text-center p-6 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
    <RouterLink
      v-for="photographia in photographiae"
      :key="photographia.id"
      :to="{ name: 'photographia', params: { id: photographia.id } }"
      class="block"
    >
      <div class="overflow-hidden rounded-t-md border border-black">
        <img
          class="aspect-square w-full object-cover object-top transition-transform duration-200 hover:scale-105"
          :src="`/imagines/photographia/${photographia.imago}`"
          :alt="photographia.titulo"
        />
      </div>
      <p class="text-black text-sm mt-1">{{ photographia.titulo }} (id: {{ photographia.id }})</p>
    </RouterLink>
  </div>
</template>


<style scoped>

</style>
