<template>
  <div>

    <h1>Detail</h1>

    <button v-if="!like" v-on:click="clickLike">좋아요</button>
    <button v-if="like" v-on:click="clickLike">좋아요 취소</button>
    <h1>제목 : {{ movie?.title }}</h1>
    <div class= "row">
      <div class="col-6">
        <img v-bind:src="ImgUrl" alt="poster" width="400" height="600" />
      </div>
      <div class="col-6" style="text-align:left">

      내용 : {{ movie?.overview }}
      
      <hr>
      장르  <li v-for= "genre in movie.genres" v-bind:key="genre" >
          {{genre.name}}
      </li>
      개봉일: {{movie?.release_date}}
      <p>
        평점:  {{movie?.vote_average}} 점
      </p>
      좋아요 수 {{likecount}}
      </div>
      

    </div>
    <a href="http://localhost:8080/movies/">영화 목록으로</a>
  </div>
</template>

<script>

import axios from "axios";

const API_URL = "http://127.0.0.1:8000";
export default {
  data() {
    return {
      username: this.$store.state.username,
      movie: null,
      like: false,
      likeusers: [],
      likecount: 0,

    };
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
    ImgUrl() {
      return `https://image.tmdb.org/t/p/original${this.movie?.poster_path}`;
    },
  },
  methods: {
    getMovieById(id) {
      for (const movie of this.movies) {
        if (movie.id === Number(id)) {
          this.movie = movie;
          break;
        }
      }
    },
    clickLike() {
      axios({
        method: "post",
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          let likeusers = res.data.like_users;
          let x = 0;
          let cnt = 0
          for (let user of likeusers) {
            if (user.username === this.username) {
              x += 1;
              cnt += 1
              this.like = true;
              break;
            }
            else{
              cnt +=1
            }
          }
          if (x === 0) {
            this.like = false;
          }
          this.likecount = cnt
        })
        .catch((err) => {
          console.log(err);
        });
    },
    LikeCheck() {
      let likeusers = this.movie.like_users;
      for (let user of likeusers) {
        if (user.username === this.username) {
          if (this.like === true) {
            this.like = false;
          } else {
            this.like = true;
          }
          this.like = true;
        }
      }
    },
  },
  created() {
    this.getMovieById(this.$route.params.id);
    this.LikeCheck();
  },
};
</script>

<style>



</style>