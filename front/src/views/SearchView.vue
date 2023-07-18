<template>
  <div>
    <h1>Search</h1>
    <input v-on:input="changeSearchTitle" v-on:keyup="isWord" type="text" />
    <button v-on:click="SearchMovie">검색</button>
    <br />
    <b-container>
      <b-row cols="5">
        <b-col v-for="movie in movies" v-bind:key="movie.id">
          <MovieListItem v-bind:movie="movie" />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import axios from "axios";
import MovieListItem from "@/components/MovieListItem.vue";
const API_URL = "http://127.0.0.1:8000";

export default {
  components: { MovieListItem },
  data() {
    return {
      SearchTitle: "",
      movies: [],
    };
  },
  methods: {
    changeSearchTitle(e) {
      this.SearchTitle = e.target.value;
    },
    isWord() {
      if (this.SearchTitle) {
        this.SearchMovie();
      }
    },
    SearchMovie() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/search/${this.SearchTitle}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.movies = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
</style>
