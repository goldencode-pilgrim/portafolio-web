<script setup lang="ts">
import { computed, ref } from 'vue';
import { useRoute } from 'vue-router';
import { photographiae } from '@/lib/photographiae';

const route = useRoute();
const zoom = ref(false);

const photographia = computed(() =>
  photographiae.find((p) => p.id === Number(route.params.id)),
);
</script>


<template>
  <div class="bg-pink-900 min-h-full w-full text-white font-sans text-center flex flex-col items-center gap-4 p-6">
    <template v-if="photographia">
      <img
        v-if="!zoom"
        class="w-full max-w-xl h-auto rounded-md border border-black cursor-zoom-in"
        :src="`/imagines/photographia/${photographia.imago}`"
        :alt="photographia.titulo"
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
          :src="`/imagines/photographia/${photographia.imago}`"
          :alt="photographia.titulo"
          title="Clic para cerrar"
        />
      </div>
      <h1 class="text-2xl font-bold">{{ photographia.titulo }}</h1>
      <p v-if="photographia.dies" class="text-sm opacity-75">Dies: {{ photographia.dies }}</p>
      <p v-if="photographia.categoria" class="text-sm opacity-75">Categoria: {{ photographia.categoria }}</p>
      <p v-if="photographia.technica" class="text-sm opacity-75">Technica: {{ photographia.technica }}</p>
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
