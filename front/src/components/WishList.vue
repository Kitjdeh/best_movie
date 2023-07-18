<template>
  <div>
    <b-container>
      <b-row cols="5">
        <b-col v-for="movie in WishListMovies" v-bind:key="movie.id">
          <MovieListItem v-bind:movie="movie" />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  props: [ "WishListMovies" ],
  components: { MovieListItem }
}
</script>

<style>

</style>