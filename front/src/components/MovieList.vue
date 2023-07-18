<template>
  <div>
    <div>
      <h1>영화</h1>
      <b-container>
        <b-row cols="5">
          <b-col v-for="perPageMovie in perPageMovies" v-bind:key="perPageMovie.id">
            <MovieListItem v-bind:movie="perPageMovie" />
          </b-col>
        </b-row>
      </b-container>
      <br>
      <b-pagination v-model="currentPage" v-bind:total-rows="rows" v-bind:per-page="perPage" align="center">
      </b-pagination>
    </div>
  </div>
</template>

<script>
import MovieListItem from "@/components/MovieListItem.vue";
export default {
  data() {
    return {
      perPage: 20,
      currentPage: 1,
    }
  },
  components: { MovieListItem },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
    perPageMovies() {
      const newMovies = this.movies.slice(
        this.perPage * this.currentPage - this.perPage,
        this.perPage * this.currentPage
      );
      return newMovies;
    },
    rows() {
      return this.movies.length;
    }
  },
  created() {
    this.$store.dispatch("getMovies");
  }
};
</script>

<style scoped>

</style>