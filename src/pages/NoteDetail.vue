<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

// 文章内容数据 — 后续可抽到独立文件
const heliumArticle = {
  title: '氦气：稀缺战略资源的产业透视',
  date: '2026-06',
  emoji: '🎈',
  tags: ['产业研究', '战略资源', '供应链'],
  sections: [
    {
      heading: '为什么关注氦气？',
      content: '氦气（Helium）是一种无色、无味、无毒的惰性气体，沸点极低（-268.9°C），是地球上已知沸点最低的物质。它在航空航天、半导体制造、医疗影像（MRI）、光纤通信、深海潜水等高科技领域具有不可替代的作用。然而，氦气在地球上属于不可再生资源，全球供应高度集中，供应链脆弱性日益凸显。',
    },
    {
      heading: '核心应用领域',
      content: '在航空航天领域，氦气用于火箭燃料加压和推进系统吹扫；在半导体行业，氦气是晶圆制造中关键的冷却介质和载气；在医疗领域，液氦是 MRI 设备超导磁体的必需冷却剂；在光纤制造中，氦气作为保护气防止气泡和杂质。这些应用几乎没有可行的替代方案，使得氦气成为高科技产业的"维生素"。',
    },
    {
      heading: '全球供应格局',
      content: '全球氦气供应高度集中于少数国家。美国、卡塔尔、俄罗斯和阿尔及利亚四国占据了全球产量的 90% 以上。氦气主要通过天然气提取获得，而非独立开采，这意味着其产量受制于天然气产业政策。近年来，美国战略氦气储备的出售、卡塔尔外交风波、俄罗斯新产能投产等因素持续扰动全球供需平衡。',
    },
    {
      heading: '中国的机遇与挑战',
      content: '中国是全球最大的氦气消费国之一，但自给率极低，长期依赖进口。近年来，中国在氦气勘探和提纯技术上取得突破，宁夏、四川等地已发现具有工业价值的富氦天然气田。然而，从勘探到商业化量产仍有较长的路要走。减少对进口氦气的依赖，是中国高端制造业必须面对的战略课题。',
    },
    {
      heading: '投资与研究视角',
      content: '从产业研究和投资角度来看，氦气供应链存在以下几个值得关注的趋势：一是氦气价格长期上行趋势明显，供需偏紧格局短期难以改变；二是氦气回收与循环利用技术将成为降本增效的关键；三是氦气替代技术（如无氦 MRI）的发展将对需求端产生影响；四是具备氦气资源和技术储备的企业可能成为产业链中的战略标的。',
    },
  ],
}

const goBack = () => {
  router.push('/notes')
}
</script>

<template>
  <div class="min-h-screen pt-24 pb-16 px-6">
    <div class="max-w-3xl mx-auto">
      
      <!-- 返回按钮 -->
      <button
        @click="goBack"
        class="inline-flex items-center gap-2 text-gray-500 hover:text-purple-600 mb-8 transition-colors"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
        返回研究笔记
      </button>

      <!-- 文章头部 -->
      <header class="mb-10">
        <div class="flex items-center gap-3 mb-4">
          <span class="text-3xl">{{ heliumArticle.emoji }}</span>
          <span class="text-sm text-gray-400">{{ heliumArticle.date }}</span>
        </div>
        <h1 class="text-3xl sm:text-4xl font-bold text-gray-800 mb-4">
          {{ heliumArticle.title }}
        </h1>
        <div class="flex flex-wrap gap-2">
          <span
            v-for="tag in heliumArticle.tags"
            :key="tag"
            class="px-3 py-1 bg-purple-50 text-purple-600 rounded-full text-xs font-medium"
          >
            {{ tag }}
          </span>
        </div>
      </header>

      <!-- 文章正文 -->
      <div class="prose prose-gray max-w-none">
        <section
          v-for="section in heliumArticle.sections"
          :key="section.heading"
          class="mb-10"
        >
          <h2 class="text-xl font-bold text-gray-800 mb-4 border-l-4 border-purple-500 pl-4">
            {{ section.heading }}
          </h2>
          <p class="text-gray-600 leading-relaxed text-lg">
            {{ section.content }}
          </p>
        </section>
      </div>

    </div>
  </div>
</template>
