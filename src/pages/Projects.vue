<script setup lang="ts">
const articles: any[] = [
  {
    slug: 'stock-002851',
    emoji: '⚡',
    title: '麦格米特 数据探索报告',
    date: '2026-06-09',
    summary: '麦格米特(sz.002851) 近2年涨超438%创历史新高。PE 565倍处于99%分位，PB 9.66倍——极端估值下的电气设备明星，是成长叙事还是泡沫狂欢？完整数据探索与深度解读。',
    tags: ['量化分析', '数据探索', '电气设备'],
  },
  {
    slug: 'stock-600879',
    emoji: '🚀',
    title: '航天电子 数据探索报告',
    date: '2026-06-09',
    summary: '航天电子(sh.600879) 近2年数据全景探索。PE/PB/PS/PCF 估值分析、季度财务拆解、多维度图表——完整展示从数据获取到可视化的量化研究流程。',
    tags: ['量化分析', '数据探索', '航天军工'],
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
