<script setup lang="ts">
import { ref } from 'vue'

const isOpen = ref(false)

const toggleMenu = () => {
  isOpen.value = !isOpen.value
}
</script>

<template>
  <nav class="fixed top-0 left-0 right-0 z-50 bg-white/80 backdrop-blur-md border-b border-gray-200">
    <div class="max-w-5xl mx-auto px-6 py-4 flex items-center justify-between">
      <!-- Logo -->
      <router-link to="/" class="text-xl font-bold text-purple-600 hover:text-purple-700 transition-colors">
        👋 大超总
      </router-link>

      <!-- Desktop Links -->
      <div class="hidden sm:flex items-center gap-8">
        <router-link to="/" class="text-gray-600 hover:text-purple-600 transition-colors">首页</router-link>
        <router-link to="/about" class="text-gray-600 hover:text-purple-600 transition-colors">关于</router-link>
        <router-link to="/projects" class="text-gray-600 hover:text-purple-600 transition-colors">项目</router-link>
      </div>

      <!-- Mobile Menu Button -->
      <button @click="toggleMenu" class="sm:hidden text-gray-600 hover:text-purple-600 p-2">
        <svg v-if="!isOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
        <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
    </div>

    <!-- Mobile Menu -->
    <div v-if="isOpen" class="sm:hidden border-t border-gray-200 bg-white/95 backdrop-blur-md">
      <div class="flex flex-col px-6 py-4 gap-4">
        <router-link to="/" @click="isOpen = false" class="text-gray-600 hover:text-purple-600 transition-colors">首页</router-link>
        <router-link to="/about" @click="isOpen = false" class="text-gray-600 hover:text-purple-600 transition-colors">关于</router-link>
        <router-link to="/projects" @click="isOpen = false" class="text-gray-600 hover:text-purple-600 transition-colors">项目</router-link>
      </div>
    </div>
  </nav>
</template>
