<script setup lang="ts">
import { House } from '@lucide/vue';

// Similar a Pavlvs.vue (vue-web): secciones a lo largo de la página con
// navegación por anclas y scroll suave.
interface Sectio {
  id: string;
  fons: string; // color de fondo de la sección
}


const sectiones: Sectio[] = [
  { id: 'Logo', fons: 'bg-[#57007f]' },
  { id: '¿Qué es la MAICI?', fons: 'bg-[#57007f]' },
  
];

const ireAdSectionem = (id: string) => {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
};
</script>


<template>
  <nav class="fixed top-0 inset-x-0 z-20 flex flex-wrap justify-center gap-4 bg-black/70 text-white py-3 px-4">
    <!-- Inicio (Domus): esquina superior izquierda del nav, como en el Layaout -->
    <RouterLink
      to="/"
      title="Domus"
      aria-label="Domus (inicio)"
      class="absolute left-1 top-1/2 -translate-y-1/2 flex items-center justify-center size-10 rounded-md bg-black hover:bg-indigo-700 transition-colors"
    >
      <House class="size-5" />
    </RouterLink>
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
    <!-- La sección Logo muestra el logo centrado; las demás, su marcador -->
    <img
      v-if="sectio.id === 'Logo'"
      class="max-w-md w-full"
      src="/imagines/maici/logo.png"
      alt="Logo MAICI"
    />

    <!-- ¿Qué es la MAICI?: cuadro grande con el texto de presentación arriba a la izquierda -->
    <div
      v-else-if="sectio.id === '¿Qué es la MAICI?'"
      class="w-3/4 min-h-[70vh] rounded-2xl border border-white/25 bg-white/10 p-8 text-left"
    >
      <p class="text-1xl md:text-2xl text-white font-medium">La MAICI <span class="font-black">(Militia Artistica Iesu Christi et Immaculate)</span> es un proyecto de apostolado católico tradicionalista enfocado a las artes.
      Cuyo propósito es organizar a los fieles católicos con voacación o interes artístico para que bajo una serie de fundamentos direccionen sus trabajos artísticos, análisis estéticos, críticas artísticas, etc.</p>
       <p class="text-1xl md:text-2xl text-white font-medium">Así como fomentar la creación de una comunidad artística católica fundamentada en la teología escolástica tradicional, para que sus miembros se apoyen entre sí y se organizen para evangelizar dichas disciplinas. Imitando para ello los modelos de otras asociaciones de fieles así como la: MI (Militia Immacualata), MJC (Militia Iesu Christi), etc.</p>
      
    </div>

    <div v-else class="w-3/4 max-w-2xl h-72 rounded-xl border border-white/25 bg-white/10"></div>
  </section>
</template>


<style scoped>

</style>
