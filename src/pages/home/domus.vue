<script setup lang="ts">

</script>

<template>
   <div class="relative isolate overflow-hidden min-h-screen w-full bg-linear-to-b from-amber-300 via-amber-800 to-violet-900 text-white font-sans text-center flex flex-col">
    <!-- Imagen de fondo: capa intermedia, siempre detrás del contenido -->
    <img class="absolute inset-0 -z-10 object-cover opacity-17 pointer-events-none" src="/imagines/domus/fondodomus.jpg"/>

    <!-- Título: banda superior, centrado y grande (como la referencia) -->
    <img
      class="mx-auto mt-9 mb-6 w-11/12 max-w-6xl"
      src="/imagines/domus/títulodomusvue.png"
      alt="Gnoseología con Golden"
    />

    <!-- Banda central: cada tesela es un RouterLink a su sección -->
    <div class="w-full h-64 bg-black grid grid-cols-7 gap-1 py-3">
      <RouterLink to="/pingo/imagines" class="block bg-gray-400 overflow-hidden group">
        <img class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105" src="/imagines/domus/pingodomus.jpg" alt="Pingo" />
      </RouterLink>
      <RouterLink to="/pictura/pinacotheca" class="block bg-gray-400 overflow-hidden group">
        <img class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105" src="/imagines/domus/pinturadomus.jpg" alt="Pintura" />
      </RouterLink>
      <RouterLink to="/photographia/pinacotheca" class="block bg-gray-400 overflow-hidden group">
        <img class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105" src="/imagines/domus/photodomus.jpg" alt="Photographia" />
      </RouterLink>
      <RouterLink to="/maici" class="block bg-gray-400 overflow-hidden group">
        <img class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105" src="/imagines/domus/maicidomus.png" alt="Maici" />
      </RouterLink>
      <RouterLink to="/pelicula/pinacotheca" class="block bg-gray-400 overflow-hidden group">
        <img class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105" src="/imagines/domus/peliculadomus.jpg" alt="Pellicula" />
      </RouterLink>
      <RouterLink to="/ludielectronici/collectione" class="block bg-gray-400 overflow-hidden group">
        <img class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105" src="/imagines/domus/videojuegosdomus.jpg" alt="Ludi electronici" />
      </RouterLink>
      <RouterLink to="/rrss" class="block bg-gray-400 overflow-hidden group">
        <img class="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105" src="/imagines/domus/rrssdomus.jpg" alt="RRSS" />
      </RouterLink>
    </div>

    <!-- Banda inferior: ocupa TODO el resto de la pantalla, a sangre, sin deformar -->
    <img
      class="w-full flex-1 min-h-0 object-cover object-bottom"
      src="/imagines/domus/footerimagedomus.png"
      alt="Ilustración de personajes"
    />
   </div>
</template>


<style scoped>

</style>
