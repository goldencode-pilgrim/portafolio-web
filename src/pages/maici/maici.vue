<script setup lang="ts">
// Similar a Pavlvs.vue (vue-web): secciones a lo largo de la página con
// navegación por anclas y scroll suave. Sin contenido: solo divs y colores.
interface Sectio {
  id: string;
  fons: string; // color de fondo de la sección
}

const sectiones: Sectio[] = [
  { id: 'prima', fons: 'bg-rose-900' },
  { id: 'secunda', fons: 'bg-indigo-950' },
  { id: 'tertia', fons: 'bg-emerald-900' },
  { id: 'quarta', fons: 'bg-amber-800' },
  { id: 'quinta', fons: 'bg-cyan-900' },
];

const ireAdSectionem = (id: string) => {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
};
</script>


<template>
  <!-- Navegación fija con anclas (como NavigatorPrimarius en Pavlvs) -->
  <nav class="fixed top-0 inset-x-0 z-20 flex flex-wrap justify-center gap-4 bg-black/70 text-white py-3 px-4">
    <button
      v-for="sectio in sectiones"
      :key="sectio.id"
      class="hover:underline"
      @click="ireAdSectionem(sectio.id)"
    >
      {{ sectio.id }}
    </button>
  </nav>

  <!-- Secciones: solo divs, un color distinto por sección -->
  <section
    v-for="sectio in sectiones"
    :id="sectio.id"
    :key="sectio.id"
    class="min-h-screen flex items-center justify-center p-6"
    :class="sectio.fons"
  >
    <div class="w-3/4 max-w-2xl h-72 rounded-xl border border-white/25 bg-white/10"></div>
  </section>
</template>


<style scoped>

</style>
