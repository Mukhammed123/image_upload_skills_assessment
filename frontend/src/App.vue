<script setup>
import { useStore } from "@/stores/rootStore";
import { useRoute, useRouter, RouterLink, RouterView } from 'vue-router'

const route = useRoute();
const router = useRouter();
const store = useStore();

const logout = () => {
  localStorage.removeItem("accessToken");
};

const accessToken = localStorage.getItem("accessToken");
if ((accessToken || "").length === 0) router.push({ path: "/sign-in" });
else store.setAccessToken(accessToken);

</script>

<template>
  <header v-if="route.path !== '/sign-in' && route.path !== '/register'">
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/sign-in" @click="logout">Logout</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style>
nav a {
  margin: 1em;
  font-size: 1.3em;
}
</style>
