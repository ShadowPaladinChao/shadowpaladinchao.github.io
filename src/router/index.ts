import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import About from '../pages/About.vue'
import Notes from '../pages/Projects.vue'
import NoteDetail from '../pages/NoteDetail.vue'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/', name: 'home', component: Home },
    { path: '/about', name: 'about', component: About },
    { path: '/notes', name: 'notes', component: Notes },
    { path: '/notes/:slug', name: 'note-detail', component: NoteDetail },
  ],
})

export default router
