<script setup lang="ts">
import { computed, ref } from 'vue';
import { useRoute } from 'vue-router';
import { delineationes } from '@/lib/delineationes';

const route = useRoute();
const zoom = ref(false);

const delineatio = computed(() =>
  delineationes.find((d) => d.id === Number(route.params.id)),
);
</script>


<template>
  <div class="bg-gray-900 min-h-full w-full text-white font-sans text-center flex flex-col items-center gap-4 p-6">
    <template v-if="delineatio">
      <img
        v-if="!zoom"
        class="w-full max-w-xl h-auto rounded-md border border-black cursor-zoom-in"
        :src="`/imagines/delineationes/${delineatio.imago}`"
        :alt="delineatio.titulo"
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
          :src="`/imagines/delineationes/${delineatio.imago}`"
          :alt="delineatio.titulo"
          title="Clic para cerrar"
        />
      </div>
      <h1 class="text-2xl font-bold italic">{{ delineatio.titulo }}</h1>
      <p v-if="delineatio.dies" class="text-sm opacity-75">Dies: {{ delineatio.dies }}</p>
      <p v-if="delineatio.categoria" class="text-sm opacity-75">Categoria: {{ delineatio.categoria }}</p>
      <p v-if="delineatio.technica" class="text-sm opacity-75">Technica: {{ delineatio.technica }}</p>
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
