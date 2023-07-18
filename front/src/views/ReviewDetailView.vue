<template>
  <div>
    <h1>ReviewDetail</h1>
    <button v-if="isAuthor" v-on:click="updateReview">수정</button>
    <button v-if="isAuthor" v-on:click="deleteReview">삭제</button>
    <div>
      영화 정보 
      <br>
      <img v-bind:src="`https://image.tmdb.org/t/p/original${this.movie?.poster_path}`" alt="" class="mini">
      <br>
      <router-link
        class="routerlink"
        v-if="review != null"
        v-bind:to="{ name: 'moviedetail', params: { id: review.movie.id } }"
        >영화 이름: {{ movie?.title }}</router-link
        >
    </div>
    <hr>
    <h5>유저 아이디: {{ review?.user.username }}</h5>
    <hr>
    <h5>리뷰 제목: {{ review?.title }}</h5>
    <hr>
    <h5>리뷰 내용</h5>
    <div>
      {{ review?.content }}
    </div>
    <hr>
    <p>{{ review?.user.username }}</p>
    <hr />
    <CommentCreate v-bind:review="review" v-on:getReview="getReview" />
    <hr />
    <CommentList
      v-bind:comments="comments"
      v-bind:review="review"
      v-on:getReview="getReview"
    />
  </div>
</template>

<script>
import axios from "axios";
import CommentCreate from "@/components/CommentCreate.vue";
import CommentList from "@/components/CommentList.vue";
const API_URL = "http://127.0.0.1:8000";

export default {
  components: { CommentCreate, CommentList },
  data() {
    return {
      comments: null,
      movie: null,
      review: null,
      isAuthor: false,
      username: this.$store.state.username,
    };
  },
  computed: {
    reviews() {
      return this.$store.state.reviews;
    },
    movies() {
      return this.$store.state.movies;
    },
  },
  methods: {
    getReview() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/reviews/${this.$route.params.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.review = res.data;
          this.comments = this.review.comments;
          console.log(1);
          console.log(this.comments);
          console.log(2);
          if (this.review.user.username === this.username) {
            this.isAuthor = true;
          }
          this.getMovieById(this.review.movie.id);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    updateReview() {
      this.$router.push({
        name: "reviewupdate",
        params: { id: this.review.id },
      });
    },
    deleteReview() {
      axios({
        method: "delete",
        url: `${API_URL}/api/v1/reviews/${this.$route.params.id}`,
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
    getMovieById(id) {
      for (const movie of this.movies) {
        if (movie.id === Number(id)) {
          this.movie = movie;
          break;
        }
      }
    },
  },
  created() {
    this.getReview();
  },
};
</script>

<style scoped>
.routerlink {
  color: #dfe5ec;
}
.mini{
  width:100px;

}
</style>