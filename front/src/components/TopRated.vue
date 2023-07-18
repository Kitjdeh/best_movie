<template>
  <div>
    <h1>Top10</h1>
    <b-container>
      <b-row cols="1">
        <VueSlickCarousel v-bind="settings">
          <b-col v-for="movie in movies.slice(0, 10)" v-bind:key="movie.id">
            <MovieListItem v-bind:movie="movie" />
          </b-col>
        </VueSlickCarousel>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel";
import "vue-slick-carousel/dist/vue-slick-carousel.css";
// optional style for arrows & dots
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css";
import MovieListItem from "@/components/MovieListItem.vue";
export default {
  components: { MovieListItem, VueSlickCarousel },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
  },
  data() {
    return {
      settings: {
        dots: true,
        infinite: true,
        slidesToShow: 5,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        pauseOnDotsHover: true,
        pauseOnFocus: true,
        pauseOnHover: true,
      },
    };
  },
};
</script>

<style>
</style>