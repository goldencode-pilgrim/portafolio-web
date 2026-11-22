<script setup lang="ts">
import { House } from '@lucide/vue';
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from '@/components/ui/accordion'

</script>

<template>
    <div class="flex h-screen">
      <nav class="w-48 shrink-0 bg-indigo-900 border-4 border-black text-white flex flex-col items-stretch gap-2.5 p-2">
       
        <RouterLink
          to="/"
          title="Domus"
          aria-label="Domus (inicio)"
          class="self-center flex items-center justify-center size-12 rounded-md bg-black hover:bg-indigo-700 transition-colors"
        >
          <House class="size-6" />
        </RouterLink>

        <!-- w-full: ocupa exactamente el ancho del nav, nunca sobresale -->
        <Accordion type="single" collapsible class="w-full">
          <AccordionItem value="secciones">
            <AccordionTrigger class="px-2">Secciones</AccordionTrigger>
            <AccordionContent class="flex flex-col gap-1 bg-indigo-800 rounded-md p-1">
              <RouterLink to="/pictura/pinacotheca" class="px-2 py-1 rounded hover:bg-indigo-700">Artes pictóricas</RouterLink>
              <RouterLink to="/pingo/imagines" class="px-2 py-1 rounded hover:bg-indigo-700">Artes gráficas</RouterLink>
              <RouterLink to="/photographia/pinacotheca" class="px-2 py-1 rounded hover:bg-indigo-700">Artes fotográficas</RouterLink>
              <RouterLink to="/pelicula/pinacotheca" class="px-2 py-1 rounded hover:bg-indigo-700">Artes audiovisuales</RouterLink>
              <RouterLink to="/ludielectronici/collectione" class="px-2 py-1 rounded hover:bg-indigo-700">Artes interactivas digitales</RouterLink>
              <RouterLink to="/maici" class="px-2 py-1 rounded hover:bg-indigo-700">MAICI</RouterLink>
              <RouterLink to="/rrss" class="px-2 py-1 rounded hover:bg-indigo-700">RR.SS</RouterLink>
            </AccordionContent>
          </AccordionItem>
        </Accordion>
      </nav>
      <main class="flex-1 overflow-y-auto">
        <RouterView />
      </main>
    </div>
</template>


<style scoped>

</style>
