<template>
  <div class ="backgound">
    <h1>Welcome</h1>
    <button v-on:click="goLogin" >Login</button>
    <p></p>
      
    <button v-on:click="goSignup">Signup</button>
    
  </div>
</template>

<script>




export default {
  data() {
    return {
      background: null,
    }
  },
  methods: {
    goLogin() {
      this.$router.push({ name: "login" });
    },
    goSignup() {
      this.$router.push({ name: "signup" });
    },
  }
};
</script>

<style>
.backgound{
  background-image: url('../assets/logo.ico.ico');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  height: 100vh;
  overflow: hidden;
}


</style>