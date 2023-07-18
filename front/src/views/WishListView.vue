<template>
  <div>
    <h1>WishList</h1>
    <br />
    <p>내가 찜 한 영화들</p>
    <WishList v-bind:WishListMovies="WishListMovies" />
    <br />
    <p>취향이 비슷한 사람들이 좋아하는 영화</p>
    <MovieRecommendedLike v-bind:LikeMovies="LikeMovies" />
    <p>유사한 장르의 영화</p>
    <MovieRecommendedGenre v-bind:GenreMovies="GenreMovies" />
  </div>
</template>

<script>
import axios from "axios";
import WishList from "@/components/WishList.vue";
import MovieRecommendedLike from "@/components/MovieRecommendedLike.vue";
import MovieRecommendedGenre from "@/components/MovieRecommendedGenre.vue";

const API_URL = "http://127.0.0.1:8000";
export default {
  components: { WishList, MovieRecommendedGenre, MovieRecommendedLike },
  data() {
    return {
      GenreMovies: [],
      LikeMovies: [],
      WishListMovies: [],
    };
  },
  methods: {
    getWishListMovies() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/wishlist/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.WishListMovies = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getGenreMovies() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/genre/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.GenreMovies = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getLikeMovies() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/likemovies/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.LikeMovies = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.getGenreMovies();
    this.getLikeMovies();
    this.getWishListMovies();
  },
};
</script>

<style>
</style>