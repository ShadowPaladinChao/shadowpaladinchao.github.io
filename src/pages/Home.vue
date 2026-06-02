<script setup lang="ts">
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-purple-500 to-pink-500">
    <div class="text-center text-white px-6 py-20">
      <h1 class="text-5xl sm:text-7xl font-bold mb-6 animate-bounce">
        👋 叫我大超总
      </h1>
      <p class="text-xl sm:text-2xl mb-4 opacity-90">
        欢迎来到我的个人网站
      </p>
      <p class="text-lg opacity-75 mb-8">
        Vue + TypeScript + Tailwind CSS 强力驱动
      </p>
      <div class="flex gap-4 justify-center flex-wrap">
        <router-link
          to="/notes"
          class="px-8 py-3 bg-white text-purple-600 rounded-full font-semibold hover:bg-gray-100 transition-colors shadow-lg"
        >
          研究笔记
        </router-link>
        <router-link
          to="/about"
          class="px-8 py-3 border-2 border-white text-white rounded-full font-semibold hover:bg-white/10 transition-colors"
        >
          关于我
        </router-link>
      </div>
    </div>
  </div>
</template>
