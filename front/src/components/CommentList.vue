<template>
  <div>
    <div v-for="comment in comments" :key="comment.id">
      <CommentItem v-bind:comment="comment" v-bind:review="review" v-on:getReview="getReview"/>
      <hr>
    </div>
  </div>
</template>

<script>
import CommentItem from '@/components/CommentItem.vue'
export default {
  props: ["comments","review"],
  components: { CommentItem },
  data() {
    return {
      isModify: false 
    }
  },
  methods: {
    getReview() {
      this.$emit('getReview')
    }
  }
}
</script>

<style>

</style>