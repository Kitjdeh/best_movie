<template>
  <div>
    <h1>MovieView</h1>
    <p>환영합니다{{ username }}님</p>
    <br />
    <TopRated v-bind:movies="topratedMovies"/>
    <br />
    <MovieList />
  </div>
</template>

<script>
import axios from "axios";
import MovieList from "@/components/MovieList.vue";
import TopRated from "@/components/TopRated.vue";
const API_URL = "http://127.0.0.1:8000";

export default {
  data() {
    return {
      username: this.$store.state.username,
      topratedMovies: null
    };
  },
  components: { MovieList, TopRated },
  methods: {
    getMovies() {
      this.$store.dispatch("getMovies");
    },
    getToprated() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/toprated/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.topratedMovies = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  // computed: {
  //   isLogin(){
  //     return this.$store.getters.isLogin
  //   }
  // },
  created() {
    this.getMovies();
  },
};
</script>
