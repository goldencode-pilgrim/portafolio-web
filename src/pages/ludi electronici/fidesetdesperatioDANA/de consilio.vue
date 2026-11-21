<script setup lang="ts">

</script>


<template>
  <!-- Similar a Circa.vue (Simpsons): figura + texto. Sin datos que no existan. -->
  <div class="flex flex-col lg:flex-row lg:justify-between items-center w-full max-w-5xl md:mx-auto my-8 gap-8 px-5 text-white">
    <figure class="relative flex justify-center items-center order-2 lg:order-1 h-[400px] lg:h-[500px] w-full max-w-[560px]">
      <!-- Imagen provisional: sustitúyela por una del juego -->
      <img
        class="object-contain h-full w-auto rounded-md"
        src="/imagines/pictura/autoretratoartista2023.jpg"
        alt="Fides et Desperatio DANA"
      />
    </figure>

    <div class="flex flex-col gap-4 order-1 text-center lg:text-left">
      <h1 class="font-bold text-xl lg:text-5xl mb-5">
        De consilio — Fides et Desperatio DANA
      </h1>

      <div class="lg:max-w-3xl">
        
        <p class="mb-5">
          Aquí irá la presentación del juego: una sinópsis general.
        </p>

        <p class="mb-5">
          créditos
        </p>
      </div>
    </div>
  </div>
</template>


<style scoped>

</style>
