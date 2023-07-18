<template>
  <div>
    <h1>Review</h1>
    <button v-on:click="goCreate">Create</button>
    <ReviewList v-bind:reviews="reviews"/>
  </div>
</template>

<script>
import ReviewList from "@/components/ReviewList.vue";
export default {
  components: { ReviewList },
  methods: {
    goCreate() {
      this.$router.push({ name: "reviewcreate" });
    },
    getReviews() {
      this.$store.dispatch("getReviews");
    },
  },
  created() {
    this.getReviews();
  },
  computed: {
    reviews() {
      return this.$store.state.reviews;
    },
  },
};
</script>

<style scoped>
</style>