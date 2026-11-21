<script setup lang="ts">
import { computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { personae } from '@/lib/personae';

const route = useRoute();
const router = useRouter();

const persona = computed(() =>
  personae.find((p) => p.id === Number(route.params.id)),
);
</script>


<template>
  <!-- Similar a Character.vue (Simpsons) en estructura básica:
       nombre + descripción + caja de cita (clic = volver) + figura. -->
  <div class="w-full max-w-5xl md:mx-auto my-8 px-5 text-white">
    <div v-if="persona" class="flex flex-col lg:flex-row lg:justify-between lg:items-center gap-8">
      <div>
        <h1 class="font-bold text-3xl lg:text-5xl mb-5">{{ persona.nomen }}</h1>

        <p
          class="text-lg lg:text-xl font-light mb-8 max-w-3xl"
          :class="persona.descriptione ? '' : 'opacity-75 italic'"
        >
          {{ persona.descriptione || 'Sin descripción todavía.' }}
        </p>

        <!-- Clic en la cita para volver a la colección (como en Character.vue) -->
        <div
          class="bg-violet-600 p-5 rounded-md border border-black flex justify-center items-center max-w-3xl cursor-pointer hover:bg-violet-500 transition-colors"
          @click="router.push({ name: 'personae' })"
        >
          <p class="text-center font-light text-2xl lg:text-3xl">
            « {{ persona.citatio || 'Sin cita todavía' }} »
          </p>
        </div>

        <RouterLink :to="{ name: 'personae' }" class="inline-block mt-6 underline opacity-80">
          ← Volver a personae
        </RouterLink>
      </div>

      <figure class="flex justify-center min-w-min">
        <img
          v-if="persona.imago"
          :src="`/imagines/ludici/${persona.imago}`"
          :alt="persona.nomen"
          class="max-h-[420px] object-contain"
        />
        <div
          v-else
          class="h-[320px] w-[240px] rounded-md border border-black bg-violet-700 flex items-center justify-center text-7xl font-bold"
        >
          {{ persona.nomen.charAt(0) }}
        </div>
      </figure>
    </div>

    <div v-else class="text-center flex flex-col items-center gap-4">
      <h1 class="font-bold text-3xl">Personaje no encontrado</h1>
      <p>No existe ningún personaje con id: {{ route.params.id }}</p>
      <RouterLink :to="{ name: 'personae' }" class="underline">← Volver a personae</RouterLink>
    </div>
  </div>
</template>


<style scoped>

</style>
