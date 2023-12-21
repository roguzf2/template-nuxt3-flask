<template>
  <v-container>
    <h1>Hello world!</h1>
    <h2>UFRJ - Analytica</h2>
    <h2>Rodrigo - Analytica</h2>
    <v-table>
      <thead>
        <tr>
          <th class="text-left">Id</th>
          <th class="text-left">Whatever</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in dados_teste" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.whatever }}</td>
        </tr>
      </tbody>
    </v-table>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue';

// Nuxt configuration
const nuxtConfig = useRuntimeConfig();

const dados_teste = ref([]);

async function updateSelectionData() {
  try {
    const response = await $fetch("/rota-teste", {
      method: "GET",
      baseURL: nuxtConfig.public.baseURL,
    });
    // Atribui os dados ao estado dados_teste
    dados_teste.value = response.results; // Certifique-se de ajustar conforme a estrutura dos dados retornados
  } catch (error) {
    console.error("Erro ao obter dados:", error);
  }
}

// onMounted hook
onMounted(updateSelectionData);
</script>
