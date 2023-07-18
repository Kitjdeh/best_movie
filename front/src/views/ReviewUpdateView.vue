<template>
  <div>
    <h1>update</h1>
    <div>
      <p>movie</p>
      <div>
        <select v-model="selected" disabled>
          <option
            v-bind:key="movie.id"
            v-bind:value="movie"
            v-for="movie in movies"
          >
            {{ movie.title }}
          </option>
        </select>
      </div>
      <p>title</p>
      <input type="text" v-model.trim="title" />
      <p>content</p>
      <input class="content" type="text" v-model="content" />
      <br />
      <button v-on:click="updateMovie">등록</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  data() {
    return {
      review: null,
      title: null,
      content: null,
      selected: null,
    };
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
    reviews() {
      return this.$store.state.reviews;
    },
  },
  methods: {
    getReviewById(id) {
      for (const review of this.reviews) {
        if (review.id === Number(id)) {
          this.review = review;
          break;
        }
      }
      this.title = this.review.title;
      this.content = this.review.content;
      this.selected = this.getMovieById(this.review.movie.id);
    },
    getMovieById(id) {
      for (const movie of this.movies) {
        if (movie.id === Number(id)) {
          return movie;
        }
      }
    },
    updateMovie() {
      const title = this.title;
      const content = this.content;
      const selected = this.selected.id;
      if (!title) {
        alert("제목을 입력해주세요.");
      } else if (!content) {
        alert("내용을 입력해주세요.");
      } else if (!selected) {
        alert("영화를 입력해주세요.");
        return;
      }
      axios({
        method: "put",
        url: `${API_URL}/api/v1/reviews/${this.$route.params.id}/`,
        data: {
          title: title,
          content: content,
          movie: selected,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.$router.push({
            name: "reviewdetail",
            params: { id: this.$route.params.id },
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.getReviewById(this.$route.params.id);
  },
};
</script>

<style>
</style>