<template>
  <div>
    <div >
      <table class="table table-sm table-dark">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">작성자</th>
            <th scope="col">글 제목</th>
            <th scope="col">댓글 수</th>
            <th scope="col">작성 날짜</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="review in reviews" v-bind:key="review.id">
            <th scope="row">{{ review.id }}</th>
            <td>{{ review.user.username }}</td>
            <td>
              <router-link class="reviewtitle" v-bind:to="{ name: 'reviewdetail', params: {id: review.id} }">{{ review.title }}</router-link>
            </td>
            <td>{{ review.comment_count }}</td>
            <td>{{ review?.created_at | moment("YYYY-MM-D h:mm:ss a")}}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>

export default {
  props:['reviews'],
  data(){
    return {
      time: this.review.created_at
    }
  },
};
</script>

<style scoped>
.reviewitem {
  display: flex;
  justify-content: space-around;
  font-size: small;
}

hr {
  height: 1px;
  background-color: #dfe5ec;
  border: 0;
}

.reviewtitle {
  color: #dfe5ec;
}
</style>