<script setup lang="ts">
import { computed, ref } from 'vue';
import { useRoute } from 'vue-router';
import { pelliculae } from '@/lib/pelliculae';

const route = useRoute();
const zoom = ref(false);

const pellicula = computed(() =>
  pelliculae.find((p) => p.id === Number(route.params.id)),
);
</script>


<template>
  <div class="bg-pink-300 min-h-full w-full text-black font-sans text-center flex flex-col items-center gap-4 p-6">
    <template v-if="pellicula">
      <img
        v-if="!zoom"
        class="w-full max-w-xl h-auto rounded-md border border-black cursor-zoom-in"
        :src="`/imagines/pellicula/${pellicula.imago}`"
        :alt="pellicula.titulo"
        title="Clic para ampliar"
        @click="zoom = true"
      />
      <div
        v-if="zoom"
        class="fixed inset-0 z-50 bg-black/90 flex items-center justify-center cursor-zoom-out"
        @click="zoom = false"
      >
        <img
          class="max-h-full max-w-full object-contain"
          :src="`/imagines/pellicula/${pellicula.imago}`"
          :alt="pellicula.titulo"
          title="Clic para cerrar"
        />
      </div>
      <h1 class="text-2xl font-bold">{{ pellicula.titulo }}</h1>
      <p v-if="pellicula.dies" class="text-sm opacity-75">Dies: {{ pellicula.dies }}</p>
      <p v-if="pellicula.categoria" class="text-sm opacity-75">Categoria: {{ pellicula.categoria }}</p>
      <p v-if="pellicula.technica" class="text-sm opacity-75">Technica: {{ pellicula.technica }}</p>
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
