<template>
  <div>
    <h1>Login</h1>
    <div>
      <p>id</p>
      <input type="text" v-model="username">
      <p>password</p>
      <input type="password" v-model="password" id="password">
      <br>


    </div>
    <br>
    <button v-on:click="logIn" >login</button>
    <br>
    <p>회원이 아니라면
      <router-link v-bind:to="{ name: 'signup' }">여기</router-link>
      를 눌러주세요
    </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn',payload)

    },
  }
}
</script>

<style>

</style>