<template>
  <div class="movieItem" v-on:mouseover="mouseOver" v-on:mouseleave="mouseLeave" v-on:click="goDetail(movie.id)">
    <div v-if="!mouseOn">
      <img class="posterImg" v-bind:src=ImgUrl width="200" height="300" >
    </div>
    <div v-if="mouseOn">
      <b-card
        v-bind:title=movie.title
        v-bind:img-src=PosterUrl
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 20rem;"
        class="mb-2"
      >
        <b-card-text class="cardtext">
          {{ movie.overview }}
        </b-card-text>

      </b-card>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mouseOn: false
    }
  },
  props: {
    movie: Object,
  },
  computed: {
    ImgUrl() {
      return `https://image.tmdb.org/t/p/original${this.movie.backdrop_path}`;
    },
    PosterUrl() {
      return `https://image.tmdb.org/t/p/original${this.movie.poster_path}`;
    },
  },
  methods: {
    goDetail(id) {
      this.$router.push({ name: "moviedetail", params: { id } });
    },
    mouseOver() {
      this.mouseOn = true
    },
    mouseLeave() {
      this.mouseOn = false
    }
  }
}
</script>

<style scoped>
.movieItem {
  margin: 10px;
}

.mb-2 {
  max-height: 30rem;
  text-overflow: ellipsis;
}

.cardtext {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  font-size: x-small;
}

.posterImg {
  object-fit: cover;
  /* image-rendering:-webkit-optimize-contrast;
  transform:translateZ(0);
  backface-visibility:hidden; */
}

</style>
