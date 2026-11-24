<script setup lang="ts">
import { computed, ref } from 'vue';
import { useRoute } from 'vue-router';
import { picturae } from '@/lib/picturae';

const route = useRoute();
const zoom = ref(false);

const cuadro = computed(() =>
  picturae.find((p) => p.id === Number(route.params.id)),
);
</script>


<template>
  <div class="bg-purple-900 min-h-full w-full text-white font-sans text-center flex flex-col items-center gap-4 p-6">
    <template v-if="cuadro">
      <img
        v-if="!zoom"
        class="w-full max-w-xl h-auto rounded-md border border-black cursor-zoom-in"
        :src="`/imagines/pictura/${cuadro.imago}`"
        :alt="cuadro.titulo"
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
          :src="`/imagines/pictura/${cuadro.imago}`"
          :alt="cuadro.titulo"
          title="Clic para cerrar"
        />
      </div>
      <h1 class="text-2xl font-bold italic">{{ cuadro.titulo }}</h1>
      <p v-if="cuadro.dies" class="text-sm opacity-75">Dies: {{ cuadro.dies }}</p>
      <p v-if="cuadro.categoria" class="text-sm opacity-75">Categoria: {{ cuadro.categoria }}</p>
      <p v-if="cuadro.technica" class="text-sm opacity-75">Technica: {{ cuadro.technica }}</p>
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
