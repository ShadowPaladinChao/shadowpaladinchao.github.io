<script setup lang="ts">
const skills = ['Vue 3', 'TypeScript', 'Tailwind CSS', 'Vite', 'Git', 'GitHub Pages']
</script>

<template>
  <div class="min-h-screen pt-24 pb-16 px-6">
    <div class="max-w-3xl mx-auto">
      <h1 class="text-4xl sm:text-5xl font-bold text-gray-800 mb-8">
        关于我
      </h1>

      <div class="prose prose-lg text-gray-600">
        <p class="text-lg mb-6">
          你好！我是大超总，一个热爱技术的前端开发者。这个网站是我用 Vue 3 + TypeScript + Tailwind CSS 搭建的个人主页。
        </p>

        <h2 class="text-2xl font-semibold text-gray-800 mt-10 mb-4">🛠️ 技能栈</h2>
        <div class="flex flex-wrap gap-3">
          <span
            v-for="skill in skills"
            :key="skill"
            class="px-4 py-2 bg-purple-100 text-purple-700 rounded-full text-sm font-medium"
          >
            {{ skill }}
          </span>
        </div>

        <h2 class="text-2xl font-semibold text-gray-800 mt-10 mb-4">📬 联系方式</h2>
        <p class="text-lg">
          你可以通过
          <a href="https://github.com/shadowpaladinchao" target="_blank" class="text-purple-600 hover:text-purple-800 underline">
            GitHub
          </a>
          找到我。
        </p>
      </div>
    </div>
  </div>
</template>
