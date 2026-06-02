<script setup lang="ts">
const projects = [
  {
    title: '个人主页',
    description: '基于 Vue 3 + TypeScript + Tailwind CSS 构建的个人网站，通过 GitHub Actions 自动部署到 GitHub Pages。',
    tags: ['Vue 3', 'TypeScript', 'Tailwind', 'GitHub Pages'],
  },
  {
    title: '更多项目',
    description: '更多精彩项目正在路上，敬请期待...',
    tags: ['Coming Soon'],
  },
]
</script>

<template>
  <div class="min-h-screen pt-24 pb-16 px-6">
    <div class="max-w-4xl mx-auto">
      <h1 class="text-4xl sm:text-5xl font-bold text-gray-800 mb-8">
        项目展示
      </h1>

      <div class="grid sm:grid-cols-2 gap-6">
        <div
          v-for="project in projects"
          :key="project.title"
          class="p-6 rounded-2xl border border-gray-200 hover:border-purple-300 hover:shadow-lg transition-all bg-white"
        >
          <h3 class="text-xl font-semibold text-gray-800 mb-3">
            {{ project.title }}
          </h3>
          <p class="text-gray-500 mb-4 leading-relaxed">
            {{ project.description }}
          </p>
          <div class="flex flex-wrap gap-2">
            <span
              v-for="tag in project.tags"
              :key="tag"
              class="px-3 py-1 bg-gray-100 text-gray-600 rounded-full text-xs font-medium"
            >
              {{ tag }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
