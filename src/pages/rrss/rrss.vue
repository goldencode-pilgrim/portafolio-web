<script setup lang="ts">
import { nexus, profilum } from '@/lib/rrss';
</script>


<template>
  <!-- Página tipo Linktree -->
  <div class="bg-gray-200 min-h-full text-black">
    <div class="max-w-md mx-auto px-4 py-10 flex flex-col items-center gap-3 text-center">
      <!-- Avatar provisional: inicial -->
      <div class="w-24 h-24 rounded-full bg-black text-white flex items-center justify-center text-4xl font-bold border-4 border-white shadow-md">
        G
      </div>

      <h1 class="text-xl font-bold mt-2">{{ profilum.nomen }}</h1>
      <p class="text-sm text-gray-600">{{ profilum.titulus }}</p>
      <p class="text-sm whitespace-pre-line">{{ profilum.bio }}</p>
      <p class="text-sm italic text-gray-700">{{ profilum.citatio }}</p>

      <!-- Enlaces (mismo orden que en el linktree original) -->
      <div class="w-full flex flex-col gap-3 mt-6">
        <template v-for="nexusItem in nexus" :key="nexusItem.id">
          <h3 v-if="nexusItem.caput" class="text-center font-bold mt-3">{{ nexusItem.caput }}</h3>
          <a
            :href="nexusItem.url"
            target="_blank"
            rel="noopener noreferrer"
            class="block w-full bg-white border border-gray-300 rounded-lg px-4 py-3 shadow-sm hover:bg-gray-50 hover:scale-[1.02] transition text-center"
          >
            <span class="font-medium">{{ nexusItem.nomen }}</span>
            <span
              v-if="nexusItem.descriptio"
              class="block text-xs text-gray-600 mt-1 whitespace-pre-line"
            >{{ nexusItem.descriptio }}</span>
          </a>
        </template>
      </div>
    </div>
  </div>
</template>


<style scoped>

</style>
