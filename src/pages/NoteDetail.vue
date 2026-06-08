<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

// 文章内容数据 — 后续可抽到独立文件或从 API 获取
const articles: Record<string, any> = {
  'stock-600879': {
    title: '航天电子 数据探索报告',
    subhead: '数据区间 2024-06-11 ~ 2026-06-08（483 个交易日）· 来源 baostock（前复权）',
    date: '2026-06-09',
    emoji: '🚀',
    tags: ['量化分析', '数据探索', '航天军工'],
    sections: [
      { heading: '公司基本信息', cards: [
        { label: '代码', value: 'sh.600879' },
        { label: '简称', value: '航天电子' },
        { label: '上市日期', value: '1995-11-15（约 31 年）' },
        { label: '行业', value: 'C37 铁路、船舶、航空航天和其他运输设备制造业' },
      ]},
      { heading: '最新行情（2026-06-08）', cards: [
        { label: '收盘价', value: '21.97 元', color: 'text-gray-800' },
        { label: '涨跌幅', value: '+2.00%', color: 'text-red-500' },
        { label: '换手率', value: '7.43%' },
        { label: '成交量', value: '24501万股' },
        { label: '成交额', value: '53.32亿' },
      ]},
      { heading: '近 2 年表现', content: '两年累计涨幅 +183.4%，但过程远非一帆风顺。2026 年 1 月 12 日触及历史最高 31.56 元后，至今回撤约 30.4%。大幅回撤往往意味着前期涨幅中存在相当比例的"情绪溢价"——当市场情绪退潮时，这部分溢价会率先蒸发。对于持有者来说，核心问题是：当前 21.97 元的价格中，有多少是基本面支撑的"内在价值"，又有多少是军工赛道溢价的"情绪价值"？', cards: [
        { label: '起始 → 当前', value: '7.03 → 21.97', sub: '+183.4%' },
        { label: '历史最高', value: '31.56', sub: '2026-01-12，回撤 -30.4%' },
      ]},
      { heading: '估值指标', content: '估值是投资决策中最核心的参考维度，但单一指标容易产生误导，需要多指标交叉验证。以下是四个关键估值指标的当前值与历史分位对比，帮助我们判断航天电子在 483 个交易日中的相对估值水平。', table: {
        headers: ['指标', '当前值', '中位数', '分位', '状态'],
        rows: [
          ['PE(TTM)', { text: '317.2', color: 'text-red-500' }, '71.8', '82%', '⚠ 高估'],
          ['PB(MRQ)', { text: '3.47', color: 'text-red-500' }, '1.57', '84%', '⚠ 高位'],
          ['PS(TTM)', { text: '5.16', color: 'text-orange-500' }, '2.48', '—', '偏高'],
          ['PCF(市现率)', { text: '-73.5', color: 'text-red-500' }, '—', '—', '⚠ 经营现金流为负'],
        ],
      }},
      { heading: '统计摘要', content: '以下是 483 个交易日中 12 项核心指标的完整描述性统计。标准差反映波动剧烈程度：PE 标准差 135.5（均值 144.7），变异系数接近 1，说明 PE 在这一时期经历了极端波动——从最低 47 到最高 533，跨度超过 10 倍。换手率同理，标准差 4.39% 超过均值 3.80%，表明市场参与热度极不均匀。这些数据共同描绘出一只高波动、事件驱动的题材型股票画像。', table: {
        headers: ['指标', '均值', '标准差', '最小', '25%', '中位', '75%', '最大'],
        rows: [
          ['开盘', '12.62', '6.29', '7.01', '8.57', '9.77', '12.00', '32.23'],
          ['最高', '12.94', '6.57', '7.10', '8.76', '9.92', '12.32', '32.24'],
          ['最低', '12.37', '6.10', '6.85', '8.46', '9.66', '11.66', '30.00'],
          ['收盘', '12.66', '6.33', '7.03', '8.62', '9.78', '12.16', '31.56'],
          ['成交量(亿)', '1.25', '1.45', '0.15', '0.42', '0.67', '1.42', '8.31'],
          ['换手率%', '3.80', '4.39', '0.47', '1.28', '2.06', '4.30', '25.18'],
          ['涨跌幅%', { text: '0.26', color: 'text-green-600' }, '3.12', { text: '-10.0', color: 'text-red-500' }, { text: '-1.47', color: 'text-red-500' }, '0.13', { text: '1.68', color: 'text-green-600' }, { text: '10.02', color: 'text-green-600' }],
          ['PE(TTM)', '144.7', '135.5', { text: '47.38', color: 'text-green-600' }, { text: '54.09', color: 'text-green-600' }, '71.81', '201.8', { text: '533.0', color: 'text-red-500' }],
          ['PB(MRQ)', '2.02', '1.00', { text: '1.14', color: 'text-green-600' }, { text: '1.38', color: 'text-green-600' }, '1.57', '1.93', { text: '5.02', color: 'text-red-500' }],
          ['PS(TTM)', '2.98', '1.56', { text: '1.30', color: 'text-green-600' }, { text: '1.96', color: 'text-green-600' }, '2.48', '3.17', { text: '7.50', color: 'text-red-500' }],
          ['PCF', { text: '-206', color: 'text-red-500' }, '680', { text: '-2210', color: 'text-red-500' }, { text: '-69.8', color: 'text-red-500' }, { text: '-52.8', color: 'text-red-500' }, { text: '58.7', color: 'text-green-600' }, { text: '695.8', color: 'text-green-600' }],
        ],
      }},
      { heading: '价格走势', content: '近两年股价从 7.03 元涨至 21.97 元，累计涨幅 +183.4%，最高触及 31.56 元（2026-01-12）。从图中可以清晰看到三段行情：2024 年下半年的底部横盘蓄力（7~9 元区间）、2025 年初至年中的主升浪（伴随成交量显著放大）、以及 2026 年 1 月见顶后的快速回落。当前价格已跌破 MA20 均线，短期均线呈空头排列，上方 25~28 元区间形成密集套牢盘，技术面偏弱。从高点回撤约 30%，但仍远高于两年均值 12.66 元，说明中长期持有者浮盈丰厚，潜在获利盘抛压不容忽视。', image: '/research/sh.600879-航天电子/exploration-20260609/explore_price.png', imageNote: '当前在 MA20 下方，空头排列' },
      { heading: '成交量 + 换手率', content: '成交量是价格的燃料。图中可见成交量峰值与价格高点高度吻合——2026 年 1 月股价冲顶 31.56 元时，单日换手率飙升至 25.18%（历史极值），成交额超 83 亿，属于典型的"天量天价"组合。此后量能持续萎缩，当前换手率 7.43% 处于 75 分位（4.30%）之上，表明交投仍较活跃，但已远不及顶部的狂热水平。值得注意的是，统计期内日均换手仅 3.80%，而近期换手率持续高于均值，说明筹码交换速度加快——这既可能是主力出货，也可能是新资金承接，需要结合价格方向综合判断。', image: '/research/sh.600879-航天电子/exploration-20260609/explore_volume.png' },
      { heading: '市盈率 PE', content: 'PE(TTM) = 股价 ÷ 近 12 月每股收益。当前 PE 为 317.2 倍，处于历史 82% 分位——意味着在过去 483 个交易日中，仅 18% 的时间估值比现在更贵。PE 中位数仅 71.81 倍，当前值是其 4.4 倍。什么概念？如果股价不变、盈利翻倍，PE 还有约 158 倍。如此高的 PE 只有两种可能：要么市场对公司未来盈利爆发式增长有极强预期（航天军工赛道的故事），要么当前价格已严重脱离基本面。从 2025 年报净利润仅 2.51 亿来看，要撑起 300+ 倍 PE，市场显然在定价"未来的航天电子"而非"现在的航天电子"。需要警惕盈利不及预期时的戴维斯双杀风险。', image: '/research/sh.600879-航天电子/exploration-20260609/explore_pe.png', imageNote: 'PE 波动 47~533，当前 317.2（82%分位），仅 18% 时间更贵' },
      { heading: '市净率 PB', content: 'PB(MRQ) = 股价 ÷ 每股净资产。当前 PB 为 3.47 倍，84% 分位，意味着市价是每股净资产的 3.47 倍。制造业 PB 通常在 1~3 倍区间，航天电子 3.47 倍的 PB 已显著高于行业中枢。回顾整个统计期，PB 最低 1.14 倍（接近破净边缘），中位数 1.57 倍，当前已是中位数的 2.2 倍。对于航天军工类企业，净资产中包含大量固定资产和政府订单相关应收款，实际变现能力可能弱于账面价值——这意味着"真实 PB"可能比 3.47 更高。', image: '/research/sh.600879-航天电子/exploration-20260609/explore_pb.png', imageNote: 'PB 波动 1.14~5.02，当前 3.47（84%分位）' },
      { heading: '市现率 PCF', content: 'PCF = 股价 ÷ 每股经营现金流。这是四个估值指标中最令人警惕的一个：当前 PCF 为 -73.5，意味着经营现金流为负——公司主营业务不仅没有产生正向现金流，反而在"烧钱"运营。统计期内 PCF 均值为 -206，中位数为 -52.8，说明经营现金流为负并非偶然，而是持续性的结构问题。航天军工企业回款周期长、存货占比高是行业特征，但长期经营现金流为负意味着：公司依赖融资或政府补贴维持运营，利润表中的"盈利"并未转化为真金白银。这一指标是判断盈利质量的关键——纸面利润再好看，没有现金流支撑也难以持续。', image: '/research/sh.600879-航天电子/exploration-20260609/explore_pcf.png', imageNote: '当前 -73.5，经营现金流为负，主营业务造血能力不足' },
      { heading: '估值全景', content: '将 PE、PB、PS 三个估值指标归一化到各自中位数=1 的基准线上，可以直观比较"谁更贵"。图中三条线均高于中位数线（=1），且 PE 的偏离度最大——当前 PE 约为中位数的 4.4 倍，PB 约为中位数的 2.2 倍，PS 约为中位数的 2.1 倍。三个指标同时高于中位数，且 PE 出现极端偏离，构成典型的"三重高估"信号。这种估值水平的公司，即便是赛道逻辑再硬，也需要业绩的超预期兑现来消化估值泡沫。', image: '/research/sh.600879-航天电子/exploration-20260609/explore_valuation.png', imageNote: 'PE/PB/PS 归一化至各自中位数=1，三指标均高于中位数，估值全面偏贵' },
      { heading: '指标分布', content: '从各指标的概率密度分布来看：① 收盘价的分布呈明显的右偏态——大部分时间股价集中在 7~15 元区间，尾部拉长到 30 元以上，反映了近期的大幅拉升；② PE 的分布最为极端，呈现"尖峰厚尾"特征，说明 PE 在大部分时间相对稳定（集中在中位数 71 附近），但少数时段出现极端值（500+），这与军工股的题材炒作特征高度吻合；③ 换手率分布同样右偏，高频换手集中在少数交易日，符合事件驱动的交易特征。整体来看，航天电子是一只"平时沉闷、风口狂暴"的典型题材驱动型标的。', image: '/research/sh.600879-航天电子/exploration-20260609/explore_dist.png' },
      { heading: '季度财务：营业收入', content: '2024-2026 年共 6 个报告期的单季营收数据显示，航天电子的营收呈现明显的季节性波动——Q4 单季营收通常为全年最高（军工企业年末集中交付结算的行业惯例），而 Q1 通常为全年最低。2025 年全年营收 139.1 亿元，各季度均有不同程度的同比增长。需要关注的是：营收增速是否在边际放缓？营收的增长是否转化为利润的增长？接下来看净利润。', image: '/research/sh.600879-航天电子/exploration-20260609/explore_quarterly_revenue.png' },
      { heading: '季度财务：净利润', content: '单季净利润的波动远大于营收。2025 年报显示全年净利润仅 2.51 亿元，对应净利润率约 1.8%——对于一个营收 139 亿的公司来说，这个利润率极薄。更关键的是，个别季度可能出现亏损或微利，这种"增收不增利"的特征在军工企业中并不罕见，但持续的低利润率意味着公司抗风险能力弱、盈利弹性低。如果营收增速放缓、成本端稍有波动，净利润可能迅速转负。', image: '/research/sh.600879-航天电子/exploration-20260609/explore_quarterly_profit.png' },
      { heading: '季度财务：毛利率', content: '毛利率反映的是产品本身的竞争力和定价权。军工企业由于客户集中（主要是军方和政府）、产品定制化程度高，毛利率通常较为稳定。从图中可以观察到毛利率的季度波动幅度——如果毛利率持续下行，可能意味着：产品结构向低毛利业务倾斜、原材料或人工成本上升、或竞争加剧导致定价能力被削弱。航天电子处于航天产业链的中上游，其毛利率水平直接反映了在产业链中的议价地位。', image: '/research/sh.600879-航天电子/exploration-20260609/explore_quarterly_margin.png' },
      { heading: '季度财务：净利率', content: '净利率 = 净利润 ÷ 营收，是衡量公司"赚钱效率"的核心指标。航天电子净利润率约 1.8%，意味着每 100 元收入中只有不到 2 元的净利润。这个数据放在制造业中也属于偏低水平——作为对比，优秀的制造业企业通常能做到 5~10% 的净利率。极低的净利率意味着公司的盈利对收入变化不敏感（经营杠杆低），股价的上涨更多依赖估值扩张而非盈利驱动——这是理解 PE 为什么能到 300+ 的关键背景：市场并非在为利润买单，而是在为"航天"这个稀缺性故事支付溢价。', image: '/research/sh.600879-航天电子/exploration-20260609/explore_quarterly_npmargin.png' },
      { heading: '季度财务：ROE', content: 'ROE（净资产收益率）= 净利润 ÷ 净资产，是巴菲特最看重的指标之一。它回答了一个根本问题：公司用股东投入的每一块钱，能赚回多少钱？航天电子当前 ROE 水平需要结合其 PB 来看——PB 3.47 倍意味着市场愿意以 3.47 倍于净资产的价格买入，如果 ROE 不能长期维持在合理水平（通常 10~15% 才算优秀），那么高 PB 就缺乏基本面支撑。关注 ROE 的季度变化趋势，如果持续低迷或下行，高估值将面临修正压力。', image: '/research/sh.600879-航天电子/exploration-20260609/explore_quarterly_roe.png' },
      { heading: '季度财务：资产负债率', content: '资产负债率反映公司的杠杆水平。军工企业由于项目周期长、回款慢、需要垫资生产，资产负债率通常偏高。适度的负债经营可以放大 ROE，但过高的负债率会增加财务风险和利息负担。需要结合有息负债占比和利息覆盖倍数来综合判断：如果负债主要来自应付账款和预收款（无息负债），则属于行业正常的经营负债；如果主要来自银行借款和债券（有息负债），则需要警惕偿债压力。航天电子作为央企背景的军工上市公司，融资渠道相对畅通，但持续为负的经营现金流意味着对外部融资的依赖度较高。', image: '/research/sh.600879-航天电子/exploration-20260609/explore_quarterly_debt.png' },
      { heading: '总结', summary: [
        { label: '价格', value: '7.03→21.97(+183.4%)，最高 31.56' },
        { label: 'PE', value: '317.2（中位 71.8），高位' },
        { label: 'PB', value: '3.47（中位 1.57），高位' },
        { label: '现金流', value: '经营现金流为负' },
        { label: '2025 年报', value: '营收 139.1 亿，净利 2.51 亿' },
      ]},
    ],
    disclaimer: '本报告由 explore_stock.py 自动生成，仅做数据展示，不构成投资建议。',
  },
  'stock-002851': {
    title: '麦格米特 数据探索报告',
    subhead: '数据区间 2024-06-11 ~ 2026-06-08（483 个交易日）· 来源 baostock（前复权）',
    date: '2026-06-09',
    emoji: '⚡',
    tags: ['量化分析', '数据探索', '电气设备'],
    sections: [
      { heading: '公司基本信息', cards: [
        { label: '代码', value: 'sz.002851' },
        { label: '简称', value: '麦格米特' },
        { label: '上市日期', value: '2017-03-06（约 9 年）' },
        { label: '行业', value: 'C38 电气机械和器材制造业' },
      ]},
      { heading: '最新行情（2026-06-08）', cards: [
        { label: '收盘价', value: '149.00 元', color: 'text-gray-800' },
        { label: '涨跌幅', value: '+1.71%', color: 'text-red-500' },
        { label: '换手率', value: '9.63%' },
        { label: '成交量', value: '4410万股' },
        { label: '成交额', value: '65.96亿' },
      ]},
      { heading: '近 2 年表现', content: '两年累计涨幅 +438.0%，从 21.77 元涨至 149.00 元，股价翻了近 7 倍。2026 年 6 月 3 日刚创下历史新高 157.98 元，当前仅回撤 5.7%。与航天电子的"冲顶回落"不同，麦格米特目前仍处于强势上攻阶段，均线多头排列，短期动能强劲。但这也意味着：如果趋势逆转，高位追入的资金将面临巨大的回撤风险——毕竟当前 PE 已高达 565 倍。', cards: [
        { label: '起始 → 当前', value: '21.77 → 149.00', sub: '+438.0%' },
        { label: '历史最高', value: '157.98', sub: '2026-06-03，仅回撤 -5.7%' },
      ]},
      { heading: '估值指标', content: '麦格米特的估值呈现出典型的"高增长高估值"特征。与航天电子（制造业、军工）不同，麦格米特属于电气设备赛道，市场给它的估值溢价更为慷慨——PE 中位数 65.5 倍本身就高于航天电子的 71.8 倍。但当前 PE 565.7 倍处于 99% 分位，意味着历史上仅 1% 的时间比现在更贵，这已不是"偏贵"可以形容，而是极端的估值水平。', table: {
        headers: ['指标', '当前值', '中位数', '分位', '状态'],
        rows: [
          ['PE(TTM)', { text: '565.7', color: 'text-red-500' }, '65.5', '99%', '⚠ 极端高估'],
          ['PB(MRQ)', { text: '9.66', color: 'text-red-500' }, '6.30', '89%', '⚠ 高位'],
          ['PS(TTM)', { text: '8.78', color: 'text-orange-500' }, '4.15', '—', '偏高'],
          ['PCF(市现率)', { text: '934.7', color: 'text-green-600' }, '37.7', '—', '经营现金流为正'],
        ],
      }},
      { heading: '统计摘要', content: '483 个交易日的完整统计描述。麦格米特的标准差极大——收盘价均值 65.78，标准差 31.99，变异系数接近 0.5，说明股价波动极为剧烈。PE 标准差 123.25（均值 126.78），说明 PE 的分布极度分散，从最低 18.07 到最高 599.84，跨度超过 30 倍。换手率均值 5.77%（航天电子为 3.80%），整体交投活跃度更高。这些数据共同指向一只高弹性、高换手、高关注的明星成长股。', table: {
        headers: ['指标', '均值', '标准差', '最小', '25%', '中位', '75%', '最大'],
        rows: [
          ['开盘', '65.62', '31.90', '21.76', '44.35', '59.94', '81.88', '155.0'],
          ['最高', '67.64', '33.04', '22.03', '45.53', '61.73', '84.92', '162.8'],
          ['最低', '63.96', '30.90', '21.68', '43.34', '58.04', '80.00', '152.9'],
          ['收盘', '65.78', '31.99', '21.77', '44.59', '59.96', '82.57', '158.0'],
          ['成交量(亿)', '0.26', '0.16', '0.02', '0.15', '0.22', '0.35', '1.08'],
          ['换手率%', '5.77', '3.53', '0.42', '3.29', '4.90', '7.58', '26.04'],
          ['涨跌幅%', { text: '0.44', color: 'text-green-600' }, '4.20', { text: '-10.0', color: 'text-red-500' }, { text: '-2.22', color: 'text-red-500' }, '0.14', { text: '2.92', color: 'text-green-600' }, { text: '10.01', color: 'text-green-600' }],
          ['PE(TTM)', '126.8', '123.3', { text: '18.07', color: 'text-green-600' }, { text: '42.15', color: 'text-green-600' }, '65.49', '181.3', { text: '599.8', color: 'text-red-500' }],
          ['PB(MRQ)', '6.25', '2.44', { text: '2.51', color: 'text-green-600' }, { text: '4.27', color: 'text-green-600' }, '6.30', '7.82', { text: '12.27', color: 'text-red-500' }],
          ['PS(TTM)', '4.22', '1.89', { text: '1.50', color: 'text-green-600' }, { text: '2.91', color: 'text-green-600' }, '4.15', '5.07', { text: '9.31', color: 'text-red-500' }],
          ['PCF', { text: '98.4', color: 'text-green-600' }, '212.0', { text: '-196', color: 'text-red-500' }, { text: '17.0', color: 'text-green-600' }, { text: '37.7', color: 'text-green-600' }, { text: '150.1', color: 'text-green-600' }, { text: '991.1', color: 'text-green-600' }],
        ],
      }},
      { heading: '价格走势', content: '近两年股价从 21.77 元涨至 149.00 元，累计涨幅 +438.0%，是航天电子涨幅（+183%）的 2.4 倍。图中可见股价始终运行在 MA20 上方，均线系统呈标准的多头排列——短期均线在上、长期均线在下，且间距逐步放大，这是典型的强势趋势行情。2025 年下半年开始出现加速上涨，斜率明显陡峭化，成交量伴随放大。当前距历史高点仅 5.7%，若突破 157.98 将打开新的上行空间；但若在此位置形成双顶结构，则需警惕趋势反转。', image: '/research/sz.002851-麦格米特/exploration-20260609/explore_price.png', imageNote: '当前在 MA20 上方，多头排列，距历史高点仅 5.7%' },
      { heading: '成交量 + 换手率', content: '成交量分布呈现明显的"量价齐升"特征。股价在 21~50 元区间时，日均换手率约 3~5%；进入 100 元以上区间后，换手率经常飙升至 10% 以上，最高达 26.04%。当前换手率 9.63% 处于 75 分位（7.58%）之上，说明市场关注度极高、筹码交换活跃。但高换手也是一把双刃剑——它既可以推动股价继续上行（新资金接力），也可能意味着主力在高位逐步派发。6 月 3 日创出天量（1.08 亿股）和天价（157.98）的组合，后续量能是否持续跟进是判断趋势持续性的关键。', image: '/research/sz.002851-麦格米特/exploration-20260609/explore_volume.png' },
      { heading: '市盈率 PE', content: 'PE(TTM) = 565.7 倍，99% 分位。这个数字意味着：以当前盈利水平，需要 565 年才能靠利润收回投资成本。当然，成长股不能这样静态地看——如果未来盈利能翻 10 倍，PE 就降到 56 倍。PE 中位数 65.5 倍本身就远高于制造业平均水平（通常 15~25 倍），说明市场一直给麦格米特较高的估值溢价。从分布来看，PE 在大部分时间处于 40~180 倍区间，当前 565 倍已是"3 个标准差之外"的极端值。能走到这一步，靠的不是利润，而是市场对电气设备赛道 + 新能源 + 智能制造的叙事定价。一旦故事褪色，估值回归中位数的幅度将是毁灭性的（从 565 到 65，意味着股价跌近 90% 才能回到"正常"估值）。', image: '/research/sz.002851-麦格米特/exploration-20260609/explore_pe.png', imageNote: 'PE 波动 18~600，当前 565.7（99%分位），仅 1% 时间更贵' },
      { heading: '市净率 PB', content: 'PB = 9.66 倍，89% 分位。每股净资产的近 10 倍——这意味着市场认为公司无形的"护城河"（技术、品牌、渠道、管理）价值远高于有形资产。电气设备行业是典型的技术密集型行业，高 PB 在一定程度上反映了其研发能力和技术壁垒。但 9.66 倍的 PB 即使在科技股中也属于高位。PB 中位数 6.30 倍，当前比中位数高出 53%。值得注意的是，PB 最低也有 2.51 倍——麦格米特从未便宜过，市场一直愿意为它支付溢价。', image: '/research/sz.002851-麦格米特/exploration-20260609/explore_pb.png', imageNote: 'PB 波动 2.51~12.27，当前 9.66（89%分位）' },
      { heading: '市现率 PCF', content: 'PCF = 934.7，经营现金流为正——这是麦格米特与航天电子最本质的区别之一。虽然 PCF 绝对数值很高（意味着每一元经营现金流对应 934 元市值），但至少说明公司主营业务在产生正向现金流。统计期内 PCF 中位数为 37.7，当前远高于中位数，反映了近期市值的快速膨胀。PCF 波动极大（均值 98.4，标准差 212），最低曾到 -196，说明部分时期也曾出现经营现金流为负的情况。总体来看，现金流状况优于航天电子（后者长期为负），但能否支撑 565 倍 PE 的估值，答案显然是否定的。', image: '/research/sz.002851-麦格米特/exploration-20260609/explore_pcf.png', imageNote: '当前 934.7，经营现金流为正但难以支撑极端估值' },
      { heading: '估值全景', content: 'PE/PB/PS 三个维度归一化后，麦格米特的估值偏移比航天电子更为剧烈。PE 约为中位数的 8.6 倍（航天电子为 4.4 倍），PB 约为 1.5 倍，PS 约为 2.1 倍。PE 的偏离度远大于 PB 和 PS，这说明问题不在资产端（PB 尚可接受），而在盈利端——当前的微薄利润完全无法支撑如此庞大的市值。市场在押注的不是"现在的麦格米特"，而是"3~5 年后的麦格米特"——假设到时利润能增长 5~10 倍，PE 就回到合理区间。但这种远期预期的定价方式，容错率极低。', image: '/research/sz.002851-麦格米特/exploration-20260609/explore_valuation.png', imageNote: 'PE/PB/PS 归一化至各自中位数=1，PE 偏离度远超 PB/PS' },
      { heading: '指标分布', content: '概率密度分布揭示了麦格米特的交易特征：① 收盘价呈明显的双峰分布——第一个峰在 40~60 元区间（2024 年底部盘整期），第二个峰在 100~140 元区间（2026 年加速上涨期），两者之间几乎没有过渡，说明股价经历了一次跳跃式的重定价；② PE 分布极度右偏，最高密度在 40~80 倍区间，但长尾延伸到 600 倍，说明大部分时间 PE 相对稳定，但近期出现了极端拉升；③ 换手率分布相对均匀，从 2% 到 15% 都有大量交易日分布，说明这只股票始终维持着较高的市场关注度。综合来看，麦格米特是一只"始终不便宜、偶尔极贵"的成长型标的。', image: '/research/sz.002851-麦格米特/exploration-20260609/explore_dist.png' },
      { heading: '季度财务：营业收入', content: '2025 年全年营收 94.0 亿元，各季度营收分布相对均匀，未出现航天电子那种明显的 Q4 集中交付特征——这与电气设备行业的订单和交付节奏更为平滑有关。营收从 2024 年到 2025 年呈现稳步增长态势，反映出公司在电源、新能源、工业自动化等领域的业务持续扩张。需要关注：营收增速是加速还是放缓？增长的质量如何（是来自核心业务还是并购/非经常性收入）？', image: '/research/sz.002851-麦格米特/exploration-20260609/explore_quarterly_revenue.png' },
      { heading: '季度财务：净利润', content: '2025 年报净利润 1.97 亿元，对应净利润率约 2.1%——比航天电子的 1.8% 略高，但仍属于极薄利润水平。净利润率薄是制造业的共性，但对于一家 PE 565 倍的公司来说，2% 的利润率意味着：即使营收翻倍，净利润也只有约 4 亿，PE 仍高达 140+ 倍。要让 PE 降到合理水平（比如 30 倍），净利润需要达到现在的 19 倍——即约 37 亿。以当前 94 亿的营收基数，这意味着净利润率需要从 2% 提升到近 40%，这在制造业几乎不可能。换言之，麦格米特的高估值逻辑，本质上不是"利润会大幅增长"，而是"市场愿意持续给高估值"。', image: '/research/sz.002851-麦格米特/exploration-20260609/explore_quarterly_profit.png' },
      { heading: '季度财务：毛利率', content: '毛利率是电气设备企业核心竞争力的体现。麦格米特的产品线涵盖电源、工业自动化、新能源车电控等，不同产品线的毛利率差异较大——电源类产品毛利率较高（30~40%），而新能源车电控等竞争激烈领域毛利率偏低。需要观察毛利率的整体趋势：如果毛利率持续提升，说明产品结构向高附加值方向优化；如果持续下降，可能是竞争加剧或原材料成本上升的信号。', image: '/research/sz.002851-麦格米特/exploration-20260609/explore_quarterly_margin.png' },
      { heading: '季度财务：净利率', content: '净利率约 2.1%，每 100 元收入中只有 2.1 元的净利润。电气设备行业属于资本和技术密集型，研发费用、销售费用和管理费用（三费）占比较高，从毛利率到净利率的"漏斗"很宽。麦格米特的费用管控能力——尤其是研发费用的资本化还是费用化处理——直接影响最终净利润的数字。投资者需要穿透利润表，理解"纸面利润"和"真实利润"之间的差距。', image: '/research/sz.002851-麦格米特/exploration-20260609/explore_quarterly_npmargin.png' },
      { heading: '季度财务：ROE', content: 'ROE 是判断高 PB 是否合理的关键。PB 9.66 倍意味着市场以近 10 倍净资产的价格买入，如果 ROE 能持续高于 15~20%，这个溢价或许可以接受。但如果 ROE 仅在个位数徘徊，那就意味着股东的每一元投入只产生几分钱的回报——这种情况下高 PB 纯粹是市场情绪驱动而非基本面驱动。关注 ROE 的季度趋势以及杜邦拆解（净利率 × 周转率 × 杠杆）来理解 ROE 的驱动因素。', image: '/research/sz.002851-麦格米特/exploration-20260609/explore_quarterly_roe.png' },
      { heading: '季度财务：资产负债率', content: '电气设备企业通常需要较大的资本开支（厂房、设备、研发），负债率是观察财务健康状况的重要窗口。适度的负债可以放大 ROE，但过高会增加财务费用和偿债风险。需要区分有息负债（银行贷款、债券）和无息负债（应付账款、预收款）——前者增加财务成本，后者反而是竞争力的体现（能占用上游供应商资金）。关注负债率的变化趋势，尤其是在营收快速扩张期，负债率是否同步攀升。', image: '/research/sz.002851-麦格米特/exploration-20260609/explore_quarterly_debt.png' },
      { heading: '总结', summary: [
        { label: '价格', value: '21.77→149.00(+438.0%)，最高 157.98（2026-06-03），多头排列' },
        { label: 'PE', value: '565.7（中位 65.5），99% 分位，极端高估' },
        { label: 'PB', value: '9.66（中位 6.30），89% 分位' },
        { label: '现金流', value: '经营现金流为正，但难以支撑当前估值' },
        { label: '2025 年报', value: '营收 94.0 亿，净利 1.97 亿，净利率 2.1%' },
        { label: '核心矛盾', value: '市场以"3~5 年后的麦格米特"定价，容错率极低；一旦增长叙事动摇，估值回归幅度巨大' },
      ]},
    ],
    disclaimer: '本报告由 explore_stock.py 自动生成，仅做数据展示，不构成投资建议。',
  },
}

const currentArticle = articles[router.currentRoute.value.params.slug as string]

const goBack = () => {
  router.push('/notes')
}
</script>

<template>
  <div class="min-h-screen pt-24 pb-16 px-6 sm:px-10 lg:px-14 text-left">

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

      <!-- 无文章时的占位 -->
      <div v-if="!currentArticle" class="text-center py-20">
        <p class="text-gray-400 text-lg">暂无此文章</p>
        <button @click="goBack" class="mt-4 text-purple-600 hover:underline">返回研究笔记</button>
      </div>

      <template v-else>
        <!-- 文章头部 -->
        <header class="mb-10">
          <div class="flex items-center gap-3 mb-4">
            <span class="text-3xl">{{ currentArticle.emoji }}</span>
            <span class="text-sm text-gray-400">{{ currentArticle.date }}</span>
          </div>
          <h1 class="text-3xl sm:text-4xl font-bold text-gray-800 mb-2">
            {{ currentArticle.title }}
          </h1>
          <p v-if="currentArticle.subhead" class="text-gray-400 text-sm mb-4">{{ currentArticle.subhead }}</p>
          <div class="flex flex-wrap gap-2">
            <span
              v-for="tag in currentArticle.tags"
              :key="tag"
              class="px-3 py-1 bg-purple-50 text-purple-600 rounded-full text-xs font-medium"
            >
              {{ tag }}
            </span>
          </div>
        </header>

        <!-- 文章正文 -->
        <div class="space-y-10">
          <section v-for="section in currentArticle.sections" :key="section.heading">
            <h2 class="text-lg font-bold text-gray-800 mb-4 border-l-4 border-purple-500 pl-3">
              {{ section.heading }}
            </h2>

            <!-- 纯文本 -->
            <p v-if="section.content" class="text-gray-600 leading-relaxed">{{ section.content }}</p>

            <!-- 卡片组 -->
            <div v-if="section.cards" class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-3">
              <div v-for="card in section.cards" :key="card.label"
                class="bg-gray-50 rounded-xl p-4 text-left">
                <p class="text-xs text-gray-400 mb-1">{{ card.label }}</p>
                <p class="text-lg font-bold" :class="card.color || 'text-gray-800'">{{ card.value }}</p>
                <p v-if="card.sub" class="text-xs text-gray-400 mt-0.5">{{ card.sub }}</p>
              </div>
            </div>

            <!-- 表格 -->
            <div v-if="section.table" class="overflow-x-auto bg-white rounded-xl border border-gray-200 shadow-sm">
              <table class="w-full text-sm">
                <thead>
                  <tr class="border-b-2 border-gray-200 bg-gray-100">
                    <th v-for="(h, hi) in section.table.headers" :key="h"
                      class="text-left py-3 px-4 font-semibold text-gray-600 first:pl-5 last:pr-5"
                      :class="hi === 0 ? '' : 'text-right'">
                      {{ h }}
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(row, ri) in section.table.rows" :key="ri"
                    class="border-b border-gray-100 last:border-0 transition-colors hover:bg-purple-50/30 odd:bg-white even:bg-gray-50/50">
                    <td v-for="(cell, ci) in row" :key="ci"
                      class="py-2.5 px-4 first:pl-5 last:pr-5 first:bg-gray-100/50 first:font-semibold first:text-gray-800"
                      :class="[ci === 0 ? '' : 'text-right font-mono tabular-nums', typeof cell === 'object' ? cell.color : 'text-gray-700']">
                      {{ typeof cell === 'object' ? cell.text : cell }}
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- 图片（单张全宽） -->
            <div v-if="section.image" class="bg-white rounded-xl border border-gray-100 p-4">
              <img :src="section.image" :alt="section.heading"
                class="w-full rounded-lg" loading="lazy" />
              <p v-if="section.imageNote" class="mt-2 text-xs text-gray-400 italic">{{ section.imageNote }}</p>
            </div>

            <!-- 总结列表 -->
            <div v-if="section.summary" class="space-y-2">
              <div v-for="item in section.summary" :key="item.label" class="flex items-start gap-3">
                <span class="shrink-0 px-2 py-0.5 bg-gray-100 text-gray-500 rounded text-xs font-medium mt-0.5">{{ item.label }}</span>
                <span class="text-gray-700 text-sm">{{ item.value }}</span>
              </div>
            </div>
          </section>
        </div>

        <!-- 免责声明 -->
        <div v-if="currentArticle.disclaimer" class="mt-10 p-4 bg-yellow-50 rounded-xl text-sm text-yellow-700">
          ⚠️ {{ currentArticle.disclaimer }}
        </div>
      </template>
  </div>
</template>
