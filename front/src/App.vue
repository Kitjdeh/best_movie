<template >
  <div id="app" class="background">
    <br />
    <nav class="navbar">
      <span class="routerlink">
        <router-link v-bind:to="{ name: 'movie' }">Home</router-link> |
        <router-link v-bind:to="{ name: 'search' }">Search</router-link> |
        <router-link v-bind:to="{ name: 'wishlist' }">WishList</router-link> |
        <router-link v-bind:to="{ name: 'review' }">Review</router-link>
      </span>
      <span v-if="this.$store.getters.isLogin" style="text-align: right">
        <span class="username">{{ username }}님</span>
        <button class="logout" v-on:click="goLogout">logout</button>
      </span>
    </nav>

    <router-view />

  </div>
</template>

<script>
export default {
  data() {
    return {
      username: this.$store.state.username,
    };
  },
  methods: {
    goLogout() {
      this.$store.dispatch("logout");
      this.accesstoken = this.$store.state.token;
    },
  },
};
</script>


<style>

* {
  background-color: #343a3f;
  color: #dfe5ec;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #dfe5ec;
}

nav {
  padding: 30px;
  /* background-color: red; */
}

nav a {
  font-weight: bold;
  color: #757676;
}

nav a.router-link-exact-active {
  color: #dfe5ec;
}

.logout {
  margin-right: 30px;
}

.routerlink {
  margin-left: 30px;
}

.username {
  margin-right: 10px;
  margin-right: 30px;
}
</style>
