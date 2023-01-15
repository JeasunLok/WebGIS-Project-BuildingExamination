<template>
  <!--<nav>
    <router-link to="/">土地利用强度监测系统</router-link> 
    <router-link to="/about"></router-link>
  </nav>
  <router-view/>
  -->
  <div id="app">
    <router-view/>
  </div>
</template>

<style>

nav {
  padding: 30px;
  /* padding: 0px; */
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
