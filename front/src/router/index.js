import Vue from 'vue'
import VueRouter from 'vue-router'
import WelcomeView from '../views/WelcomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import MovieView from '../views/MovieView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import SearchView from '../views/SearchView.vue'
import WishListView from '../views/WishListView.vue'
import ReviewView from '../views/ReviewView.vue'
import ReviewDetailView from '../views/ReviewDetailView.vue'
import ReviewCreateView from '../views/ReviewCreateView.vue'
import ReviewUpdateView from '../views/ReviewUpdateView.vue'
import store from '@/store/index'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'welcome',
    component: WelcomeView,
    meta: { requireAuth: false },
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    meta: { requireAuth: false },
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView,
    meta: { requireAuth: false },
  },
  {
    path: '/movies',
    name: 'movie',
    component: MovieView,
    meta: { requireAuth: true },
  },
  {
    path: '/movies/:id',
    name: 'moviedetail',
    component: MovieDetailView,
    meta: { requireAuth: true },
  },
  {
    path: '/movies/search',
    name: 'search',
    component: SearchView,
    meta: { requireAuth: true },
  },
  {
    path: '/movies/wishlist',
    name: 'wishlist',
    component: WishListView,
    meta: { requireAuth: true },
  },
  {
    path: '/reviews',
    name: 'review',
    component: ReviewView,
    meta: { requireAuth: true },
  },
  {
    path: '/reviews/:id',
    name: 'reviewdetail',
    component: ReviewDetailView,
    meta: { requireAuth: true },
  },
  {
    path: '/reviews/create',
    name: 'reviewcreate',
    component: ReviewCreateView,
    meta: { requireAuth: true },
  },
  {
    path: '/reviews/:id/update',
    name: 'reviewupdate',
    component: ReviewUpdateView,
    meta: { requireAuth: true },
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    const loginStatus = store.getters.isLogin
    if (!loginStatus) {
      alert("로그인 후 이용해주세요.");
      next({ name: 'login' });
    } else {
			next({path: {name: 'movie'}});
		}
	} else {
		next();
	}

});

export default router
