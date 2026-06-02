<script setup lang="ts">
const interests = [
  { emoji: '⚙️', name: '工程技术' },
  { emoji: '🚀', name: '航空航天' },
  { emoji: '🤖', name: 'AI 技术' },
  { emoji: '📊', name: '产业研究' },
  { emoji: '💰', name: '投资理财' },
]

const skillGroups = [
  {
    icon: '⚙️', title: '工程技术',
    skills: ['CAD', 'MATLAB', 'Python'],
  },
  {
    icon: '🚀', title: '航空航天',
    skills: ['飞行力学', '推进系统', '空气动力学'],
  },
  {
    icon: '🤖', title: 'AI 技术',
    skills: ['PyTorch', '机器学习', '深度学习'],
  },
  {
    icon: '📊', title: '产业研究',
    skills: ['数据分析', '行业研究', '市场调研'],
  },
  {
    icon: '💰', title: '投资理财',
    skills: ['财务分析', '资产配置', '风险管理'],
  },
  {
    icon: '💻', title: 'Web 开发',
    skills: ['Vue 3', 'TypeScript', 'Tailwind CSS', 'Vite', 'Git'],
  },
]
</script>

<template>
  <div class="min-h-screen pt-24 pb-16 px-6">
    <div class="max-w-5xl mx-auto">
      <!-- 左右布局 -->
      <div class="flex flex-col md:flex-row gap-12">
        
        <!-- 左侧：个人信息卡片 -->
        <div class="md:w-80 shrink-0">
          <div class="sticky top-24 bg-white rounded-2xl border border-gray-200 p-8 text-center shadow-sm">
            <!-- 头像 -->
            <img
              src="https://github.com/shadowpaladinchao.png"
              alt="头像"
              class="w-32 h-32 mx-auto mb-6 rounded-full shadow-lg object-cover border-4 border-purple-200"
            />
            
            <h2 class="text-2xl font-bold text-gray-800 mb-1">叫我大超总</h2>
            <p class="text-purple-600 font-medium mb-6">工程师</p>
            
            <!-- 社交链接 -->
            <div class="flex justify-center gap-4">
              <a href="https://github.com/shadowpaladinchao" target="_blank"
                class="w-10 h-10 rounded-full bg-gray-100 hover:bg-gray-800 hover:text-white flex items-center justify-center transition-colors text-gray-600">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
                </svg>
              </a>
              <a href="mailto:thuyaochao@gmail.com"
                class="w-10 h-10 rounded-full bg-gray-100 hover:bg-purple-500 hover:text-white flex items-center justify-center transition-colors text-gray-600">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                </svg>
              </a>
            </div>
          </div>
        </div>

        <!-- 右侧：详细信息 -->
        <div class="flex-1 space-y-8">
          
          <!-- 关于我 -->
          <section>
            <h3 class="text-2xl font-bold text-gray-800 mb-4 flex items-center gap-2">
              <span>👋</span> 关于我
            </h3>
            <p class="text-gray-600 leading-relaxed text-lg">
              你好！我是一名工程师，对工程技术、航空航天和 AI 技术充满热情。同时也关注产业研究与投资理财。这个网站是我用 Vue 3 + TypeScript + Tailwind CSS 搭建的个人主页，记录我的思考与项目。
            </p>
          </section>

          <!-- 兴趣领域 -->
          <section>
            <h3 class="text-2xl font-bold text-gray-800 mb-4 flex items-center gap-2">
              <span>🎯</span> 兴趣领域
            </h3>
            <div class="grid grid-cols-2 sm:grid-cols-3 gap-3">
              <div v-for="item in interests" :key="item.name"
                class="flex items-center gap-3 p-4 rounded-xl border border-gray-200 hover:border-purple-300 hover:shadow-md transition-all bg-white">
                <span class="text-2xl">{{ item.emoji }}</span>
                <span class="text-gray-700 font-medium">{{ item.name }}</span>
              </div>
            </div>
          </section>

          <!-- 技能栈 -->
          <section>
            <h3 class="text-2xl font-bold text-gray-800 mb-4 flex items-center gap-2">
              <span>🛠️</span> 技能栈
            </h3>
            <div class="grid sm:grid-cols-2 gap-4">
              <div v-for="group in skillGroups" :key="group.title"
                class="p-5 rounded-xl border border-gray-200 bg-white hover:shadow-md transition-shadow">
                <h4 class="text-sm font-bold text-gray-800 mb-3 flex items-center gap-2">
                  <span class="text-lg">{{ group.icon }}</span>
                  {{ group.title }}
                </h4>
                <div class="flex flex-wrap gap-2">
                  <span v-for="skill in group.skills" :key="skill"
                    class="px-3 py-1.5 bg-gradient-to-r from-purple-50 to-pink-50 text-purple-700 rounded-full text-xs font-medium border border-purple-200">
                    {{ skill }}
                  </span>
                </div>
              </div>
            </div>
          </section>

          <!-- 联系方式 -->
          <section>
            <h3 class="text-2xl font-bold text-gray-800 mb-4 flex items-center gap-2">
              <span>📬</span> 联系方式
            </h3>
            <div class="flex flex-wrap gap-4">
              <a href="https://github.com/shadowpaladinchao" target="_blank"
                class="inline-flex items-center gap-2 px-5 py-3 bg-gray-800 text-white rounded-xl hover:bg-gray-700 transition-colors">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
                </svg>
                GitHub
              </a>
              <a href="mailto:thuyaochao@gmail.com"
                class="inline-flex items-center gap-2 px-5 py-3 bg-purple-600 text-white rounded-xl hover:bg-purple-500 transition-colors">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                </svg>
                thuyaochao@gmail.com
              </a>
            </div>
          </section>

        </div>
      </div>
    </div>
  </div>
</template>
