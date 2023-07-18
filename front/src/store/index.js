import Vue from "vue"
import Vuex from "vuex"
import createPersistedState from 'vuex-persistedstate'
import axios from "axios"
// import moviedata from '../moviedata.json'
import router from "@/router"


Vue.use(Vuex);

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins:[
    createPersistedState()
  ],
  state: {
    movies: [],
    reviews: [],
    token: null,
    username: "",
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_REVIEWS(state, reviews) {
      state.reviews = reviews
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'movie' })
    },
    GET_LOGOUT(state) {
      state.user = null
      state.token = null
      state.username = ""
      console.log('GETLOTOUT까지옴')
      alert('logout 성공! 안녕히 가세요')
      
      router.push({ name: 'welcome' })
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method:'get',
        url: `${API_URL}/api/v1/movies`,
        // headers: {
        //   Authorization: `Token ${context.state.token}`
        // }
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getReviews(context) {
      axios({
        method:'get',
        url: `${API_URL}/api/v1/reviews`,
        // headers: {
        //   Authorization: `Token ${context.state.token}`
        // }
      })
        .then((res) => {
          context.commit('GET_REVIEWS', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          this.state.username = payload.username
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    logout(context) {
      console.log('commit까지옴')
      
      context.commit('GET_LOGOUT')
    },
  },
  modules: {},
});
