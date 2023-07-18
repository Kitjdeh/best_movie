<template>
  <div>
    <h1>Review Create</h1>
    <div>
      <p>movie</p>
      <div>
        <select v-model="selected">
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
    </div>
    <br />
    <button v-on:click="createReview">Submit</button>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  data() {
    return {
      title: null,
      content: null,
      selected: null,
    };
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
    // users() {
    //   return this.$store.state.
    // }
  },
  methods: {
    createReview() {
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
        method: "post",
        url: `${API_URL}/api/v1/reviews/`,
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
          this.$router.push({ name: "review" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
.content {
  height: 100px;
}
</style>