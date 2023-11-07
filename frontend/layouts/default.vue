<template>
  <v-app>
    <v-app-bar :elevation="1">
      <v-spacer></v-spacer>
      <span>
        <v-icon icon="mdi:mdi-vuetify"></v-icon>
        <b> Nuxt.js Template</b>
      </span>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main>
      <slot></slot>
    </v-main>

    <v-footer app border>
      This is a footer! @ {{ new Date().getFullYear() }}
    </v-footer>
  </v-app>
</template>
