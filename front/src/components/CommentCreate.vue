<template>
  <div>
    <input type="text" v-model="content">
    <button v-on:click="createComment">등록</button>
  </div>
</template>

<script>
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default {
  props: ["review"],
  data() {
    return {
      content: null,
    }
  },
  methods: {
    createComment() {
      const content = this.content
      const review = this.review.id
      if (!content) {
        alert('내용을 입력해주세요.')
        return
      } 
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/reviews/${review}/comment/`,
        data: {
          content: content,
          review: review,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.content = null
          this.$emit('getReview')
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
}
</script>

<style>

</style>