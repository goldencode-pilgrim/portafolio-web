<script setup lang="ts">
import { useRouter } from 'vue-router';
import { personae } from '@/lib/personae';

const router = useRouter();
</script>


<template>
  <!-- Similar a Colectione.vue (Simpsons) pero básico: sin paginación ni Card,
       con marcador inicial cuando no hay imagen. -->
  <div class="flex flex-col items-center gap-8 w-full max-w-5xl my-8 mx-auto text-white">
    <div class="text-center">
      <h1 class="font-bold text-xl lg:text-5xl mb-3">Personae</h1>
      <p class="mb-5 opacity-80">Elige un personaje para ver su ficha</p>
    </div>

    <div class="grid grid-cols-2 md:grid-cols-3 gap-8 mx-auto">
      <div
        v-for="persona in personae"
        :key="persona.id"
        class="cursor-pointer w-[220px] h-[240px] rounded-md border border-black bg-violet-950 hover:bg-violet-600 transition-colors flex flex-col items-center justify-center gap-2 px-2"
        @click="router.push(`/ludielectronici/f&d-dana/personae${persona.id}`)"
      >
        <img
          v-if="persona.imago"
          class="h-[160px] w-[160px] object-cover object-top rounded-t-md border border-black"
          :src="`/imagines/ludici/${persona.imago}`"
          :alt="persona.nomen"
        />
        <div
          v-else
          class="h-[160px] w-[160px] rounded-t-md border border-black bg-violet-700 flex items-center justify-center text-5xl font-bold"
        >
          {{ persona.nomen.charAt(0) }}
        </div>
        <h2 class="font-medium text-lg">{{ persona.nomen }}</h2>
      </div>
    </div>
  </div>
</template>


<style scoped>

</style>
