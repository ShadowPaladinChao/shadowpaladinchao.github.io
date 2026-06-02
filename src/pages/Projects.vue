<script setup lang="ts">
const articles = [
  {
    slug: 'helium',
    emoji: '🎈',
    title: '氦气：稀缺战略资源的产业透视',
    date: '2026-06',
    summary: '从航空航天到半导体，从 MRI 到光纤制造——氦气是不可替代的高科技"维生素"。探讨全球供应格局、中国的机遇与挑战。',
    tags: ['产业研究', '战略资源', '供应链'],
  },
]
</script>

<template>
  <div class="min-h-screen pt-24 pb-16 px-6">
    <div class="max-w-3xl mx-auto">
      
      <div class="mb-10">
        <h1 class="text-4xl sm:text-5xl font-bold text-gray-800 mb-3">
          📝 研究笔记
        </h1>
        <p class="text-gray-500 text-lg">
          产业研究 · 技术洞察 · 投资思考
        </p>
      </div>

      <div class="space-y-4">
        <router-link
          v-for="article in articles"
          :key="article.slug"
          :to="`/notes/${article.slug}`"
          class="block group p-6 rounded-2xl border border-gray-200 bg-white hover:border-purple-300 hover:shadow-lg transition-all"
        >
          <div class="flex items-start gap-4">
            <span class="text-3xl shrink-0 mt-1">{{ article.emoji }}</span>
            <div class="flex-1 min-w-0">
              <div class="flex items-center gap-3 mb-2">
                <h3 class="text-lg font-bold text-gray-800 group-hover:text-purple-600 transition-colors">
                  {{ article.title }}
                </h3>
                <span class="text-xs text-gray-400 shrink-0">{{ article.date }}</span>
              </div>
              <p class="text-gray-500 leading-relaxed mb-3">
                {{ article.summary }}
              </p>
              <div class="flex flex-wrap gap-2">
                <span
                  v-for="tag in article.tags"
                  :key="tag"
                  class="px-2.5 py-1 bg-purple-50 text-purple-600 rounded-full text-xs font-medium"
                >
                  {{ tag }}
                </span>
              </div>
            </div>
          </div>
        </router-link>
      </div>

    </div>
  </div>
</template>
