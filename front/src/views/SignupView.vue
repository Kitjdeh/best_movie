<template>
  <div>
    <h1>Signup</h1>
    <div>
      <p>아이디</p>
      <input type="text" v-model="username" />
      <p>비밀번호</p>
      <input type="password" v-model="password1" />
      <p>비밀번호 확인</p>
      <input type="password" v-model="password2" />
    </div>
    <br />
    <button v-on:click="signUp">login</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    };
  },
  methods: {
    signUp() {
      const username = this.username;
      const password1 = this.password1;
      const password2 = this.password2;

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      };

      this.$store.dispatch("signUp", payload);
    },
  },
};
</script>

<style>
</style>