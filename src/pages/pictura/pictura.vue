<script setup lang="ts">
import { picturae } from '@/lib/picturae';
</script>


<template>
  <div class="bg-gray-300 min-h-full w-full font-sans text-center p-6 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
    <RouterLink
      v-for="pictura in picturae"
      :key="pictura.id"
      :to="{ name: 'pinturas', params: { id: pictura.id } }"
      class="block"
    >
      <div class="overflow-hidden rounded-t-md border border-black">
        <img
          class="aspect-square w-full object-cover object-top transition-transform duration-200 hover:scale-105"
          :src="`/imagines/pictura/${pictura.imago}`"
          :alt="pictura.titulo"
        />
      </div>
      <p class="text-black text-sm mt-1">{{ pictura.titulo }} (id: {{ pictura.id }})</p>
    </RouterLink>
  </div>
</template>


<style scoped>

</style>
