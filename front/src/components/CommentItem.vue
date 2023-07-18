<template>
  <div>
    <div v-if="!isModify">
      <span>댓글 User: {{ comment.user.username }}</span> |
      <span>댓글 내용: {{ comment.content }}</span> |
      <span v-if="comment.user.username === this.$store.state.username">
        <button v-on:click="changeComment">수정</button> |
        <button v-on:click="deleteComment">삭제</button> |
      </span>
    </div>
    <div v-if="isModify">
      <input type="text" v-model="content" />
      <button v-on:click="updateComment">등록</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  props: ["comment", "review"],
  data() {
    return {
      isModify: false,
      content: this.comment.content,
    };
  },
  methods: {
    changeComment() {
      this.isModify = true;
      this.$emit("getReview");
    },
    updateComment() {
      const content = this.content;
      const review = this.review.id;
      if (!content) {
        alert("내용을 입력해주세요.");
        return;
      }
      axios({
        method: "put",
        url: `${API_URL}/api/v1/reviews/${review}/comment/${this.comment.id}/`,
        data: {
          content: content,
          review: review,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.isModify = false;
          this.$emit("getReview");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteComment() {
      axios({
        method: "delete",
        url: `${API_URL}/api/v1/reviews/${this.review.id}/comment/${this.comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then(() => {
          this.$emit("getReview");
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