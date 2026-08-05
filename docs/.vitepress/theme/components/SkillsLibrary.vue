<script setup lang="ts">
import { ref } from "vue";

interface Skill {
  name: string;
  file: string;
}

interface Category {
  id: number;
  emoji: string;
  name: string;
  tags: string;
  color: string;
  skills: Skill[];
}

const categories: Category[] = [
  {
    id: 1,
    emoji: "📐",
    name: "备课·课程设计",
    tags: "教案/课程开发/单元规划",
    color: "#4add86",
    skills: [
      { name: "逆向设计单元规划", file: "01-逆向设计单元规划.md" },
      { name: "学习进阶构建", file: "02-学习进阶构建.md" },
      { name: "课堂导入设计", file: "03-课堂导入设计.md" },
      { name: "课程设计师", file: "04-课程设计师.md" },
      { name: "课程创建工具", file: "05-课程创建工具.md" },
      { name: "专业教育课程设计", file: "06-专业教育课程设计.md" },
      { name: "课程创建流程", file: "07-课程创建流程.md" },
      { name: "课程教案构建器", file: "08-课程教案构建器.md" },
      { name: "台湾108课纲教案", file: "09-台湾108课纲教案.md" },
      { name: "项目简报设计", file: "10-项目简报设计.md" },
      { name: "UDL课程审计", file: "11-UDL课程审计.md" },
    ],
  },
  {
    id: 2,
    emoji: "🎯",
    name: "课堂教学",
    tags: "导入/直接教学/检查理解/提问",
    color: "#f59e0b",
    skills: [
      { name: "检查理解协议", file: "01-检查理解协议.md" },
      { name: "直接教学序列", file: "02-直接教学序列.md" },
      { name: "练习题序列设计", file: "03-练习题序列设计.md" },
      { name: "关键节点提问", file: "04-关键节点提问.md" },
      { name: "苏格拉底式提问", file: "05-苏格拉底式提问.md" },
      { name: "讨论协议选择", file: "06-讨论协议选择.md" },
      { name: "分层教学适配器", file: "07-分层教学适配器.md" },
    ],
  },
  {
    id: 3,
    emoji: "🧠",
    name: "记忆·学习科学",
    tags: "间隔/提取/交错/双重编码",
    color: "#8b5cf6",
    skills: [
      { name: "间隔练习排程器", file: "01-间隔练习排程器.md" },
      { name: "提取练习生成器", file: "02-提取练习生成器.md" },
      { name: "交错练习单元规划", file: "03-交错练习单元规划.md" },
      { name: "认知负荷分析器", file: "04-认知负荷分析器.md" },
      { name: "双重编码设计", file: "05-双重编码设计.md" },
    ],
  },
  {
    id: 4,
    emoji: "📊",
    name: "评估·批改",
    tags: "形成性评估/量规/缺口分析/题库",
    color: "#ef4444",
    skills: [
      { name: "形成性评估技术选择", file: "01-形成性评估技术选择.md" },
      { name: "标准参照量规生成", file: "02-标准参照量规生成.md" },
      { name: "学生作业缺口分析", file: "03-学生作业缺口分析.md" },
      { name: "单点量规设计", file: "04-单点量规设计.md" },
      { name: "考试题目生成器", file: "05-考试题目生成器.md" },
      { name: "错误分析协议", file: "06-错误分析协议.md" },
    ],
  },
  {
    id: 5,
    emoji: "📚",
    name: "读写·学科技能",
    tags: "阅读/写作/英语/项目",
    color: "#06b6d4",
    skills: [
      { name: "阅读理解策略", file: "01-阅读理解策略.md" },
      { name: "论证结构脚手架", file: "02-论证结构脚手架.md" },
      { name: "文本复杂度分析", file: "03-文本复杂度分析.md" },
      { name: "词汇分层工具", file: "04-词汇分层工具.md" },
      { name: "学术语言句型框架", file: "05-学术语言句型框架.md" },
      { name: "学习策略选择", file: "06-学习策略选择.md" },
      { name: "深度学习PyTorch", file: "07-深度学习PyTorch.md" },
    ],
  },
  {
    id: 6,
    emoji: "🔬",
    name: "教研·论文",
    tags: "课例研究/听评课/反思/深度研究",
    color: "#ec4899",
    skills: [
      { name: "听评课协议", file: "01-听评课协议.md" },
      { name: "课例研究周期", file: "02-课例研究周期.md" },
      { name: "反思实践提示", file: "03-反思实践提示.md" },
      { name: "教师探究周期", file: "04-教师探究周期.md" },
      { name: "学科教学知识发展", file: "05-学科教学知识发展.md" },
      { name: "教学辅导对话指南", file: "06-教学辅导对话指南.md" },
      { name: "多源深度研究", file: "07-多源深度研究.md" },
    ],
  },
  {
    id: 7,
    emoji: "💝",
    name: "班级·学生身心",
    tags: "动机/自我效能/归属感/修复式实践",
    color: "#f472b6",
    skills: [
      { name: "动机诊断与任务再设计", file: "01-动机诊断与任务再设计.md" },
      { name: "自我效能感构建", file: "02-自我效能感构建.md" },
      { name: "归属感班级文化设计", file: "03-归属感班级文化设计.md" },
      { name: "实施意图设计", file: "04-实施意图设计.md" },
      { name: "修复式实践协议", file: "05-修复式实践协议.md" },
      { name: "Canva课堂助手", file: "06-Canva课堂助手.md" },
    ],
  },
  {
    id: 8,
    emoji: "🛡️",
    name: "AI 素养",
    tags: "AI输出审计/幻觉核查/教育注释",
    color: "#6366f1",
    skills: [
      { name: "AI输出审计设计", file: "01-AI输出审计设计.md" },
      { name: "AI幻觉事实核查协议", file: "02-AI幻觉事实核查协议.md" },
      { name: "代码教育注释", file: "03-代码教育注释.md" },
    ],
  },
  {
    id: 9,
    emoji: "⚙️",
    name: "治理·决策",
    tags: "PD/推论阶梯/课程审计/杠杆点",
    color: "#14b8a6",
    skills: [
      { name: "教师PD培训设计", file: "01-教师PD培训设计.md" },
      { name: "推论阶梯反思", file: "02-推论阶梯反思.md" },
      { name: "杠杆点与响应设计", file: "03-杠杆点与响应设计.md" },
      { name: "心智模型映射", file: "04-心智模型映射.md" },
      { name: "课程覆盖审计", file: "05-课程覆盖审计.md" },
    ],
  },
  {
    id: 10,
    emoji: "🎬",
    name: "内容创作",
    tags: "PPT/视频/动画/交互课件",
    color: "#f97316",
    skills: [
      { name: "HTML-PPT-Studio", file: "01-HTML-PPT-Studio.md" },
      { name: "K12互动课件开发", file: "02-K12互动课件开发.md" },
      { name: "教育演示文稿制作", file: "03-教育演示文稿制作.md" },
      { name: "交互式HTML-React课件", file: "04-交互式HTML-React课件.md" },
      { name: "教育视频创作", file: "05-教育视频创作.md" },
      { name: "Manim动画规划", file: "06-Manim动画规划.md" },
      { name: "Manim动画生成", file: "07-Manim动画生成.md" },
      { name: "Three.js-3D几何", file: "08-Three.js-3D几何.md" },
      { name: "Remotion视频工具包", file: "09-Remotion视频工具包.md" },
      { name: "动画原理教育", file: "10-动画原理教育.md" },
    ],
  },
  {
    id: 11,
    emoji: "🎓",
    name: "学伴·通识",
    tags: "K12全科/教育角色/项目营销",
    color: "#84cc16",
    skills: [
      { name: "K12数学全科辅导", file: "01-K12数学全科辅导.md" },
      { name: "K12理科", file: "02-K12理科.md" },
      { name: "K12语言", file: "03-K12语言.md" },
      { name: "K12考试体系备考", file: "04-K12考试体系备考.md" },
      { name: "通用学习助手", file: "05-通用学习助手.md" },
      { name: "教育专家角色", file: "06-教育专家角色.md" },
    ],
  },
];

const expandedId = ref<number | null>(null);

function toggle(id: number) {
  expandedId.value = expandedId.value === id ? null : id;
}

function getDownloadPath(cat: Category, skill: Skill): string {
  const catDir = String(cat.id).padStart(2, "0") + "-" + getCategoryDirName(cat.id);
  return `/skills/${catDir}/${skill.file}`;
}

function getCategoryDirName(id: number): string {
  const names: Record<number, string> = {
    1: "备课与课程设计",
    2: "课堂教学",
    3: "记忆与学习科学",
    4: "评估与批改",
    5: "读写与学科",
    6: "教研与论文",
    7: "班级与学生身心",
    8: "AI素养",
    9: "治理与决策",
    10: "内容创作",
    11: "学伴与通识",
  };
  return names[id] || "";
}

const totalSkills = categories.reduce((sum, cat) => sum + cat.skills.length, 0);
</script>

<template>
  <div class="skills-library">
    <div class="skills-header">
      <h2 class="skills-title">📦 Skills 工具库</h2>
      <p class="skills-subtitle">
        共 <strong>{{ totalSkills }}</strong> 个 Skill，覆盖
        <strong>{{ categories.length }}</strong> 大教学功能分类，点击分类展开查看详情
      </p>
    </div>

    <div class="skills-grid">
      <div
        v-for="cat in categories"
        :key="cat.id"
        class="skill-card"
        :class="{ expanded: expandedId === cat.id }"
        :style="{ '--card-color': cat.color }"
        @click="toggle(cat.id)"
      >
        <div class="card-top-border" :style="{ backgroundColor: cat.color }"></div>
        <div class="card-body">
          <div class="card-header">
            <span class="card-emoji">{{ cat.emoji }}</span>
            <div class="card-info">
              <h3 class="card-name">{{ cat.name }}</h3>
              <p class="card-tags">{{ cat.tags }}</p>
            </div>
            <span class="card-count">{{ cat.skills.length }}</span>
          </div>

          <transition name="slide">
            <div v-if="expandedId === cat.id" class="card-skills" @click.stop>
              <div
                v-for="skill in cat.skills"
                :key="skill.file"
                class="skill-item"
              >
                <span class="skill-name">{{ skill.name }}</span>
                <a
                  :href="getDownloadPath(cat, skill)"
                  download
                  class="skill-download"
                  :title="`下载 ${skill.name}`"
                >
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                    <polyline points="7 10 12 15 17 10"/>
                    <line x1="12" y1="15" x2="12" y2="3"/>
                  </svg>
                </a>
              </div>
            </div>
          </transition>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.skills-library {
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px 0;
}

.skills-header {
  text-align: center;
  margin-bottom: 32px;
}

.skills-title {
  font-size: 28px;
  font-weight: 700;
  color: var(--wb-ink, #11130e);
  margin: 0 0 8px;
}

.skills-subtitle {
  font-size: 15px;
  color: var(--wb-muted, #656b60);
  margin: 0;
}

.skills-subtitle strong {
  color: var(--wb-acid-strong, #34c674);
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

@media (max-width: 1024px) {
  .skills-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 640px) {
  .skills-grid {
    grid-template-columns: 1fr;
  }
}

.skill-card {
  background: var(--wb-surface, #ffffff);
  border: 1px solid var(--wb-line, #d7dbd0);
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.skill-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.skill-card.expanded {
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
}

.card-top-border {
  height: 4px;
  width: 100%;
}

.card-body {
  padding: 16px;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 10px;
}

.card-emoji {
  font-size: 28px;
  flex-shrink: 0;
}

.card-info {
  flex: 1;
  min-width: 0;
}

.card-name {
  font-size: 15px;
  font-weight: 600;
  color: var(--wb-ink, #11130e);
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.card-tags {
  font-size: 12px;
  color: var(--wb-muted, #656b60);
  margin: 2px 0 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.card-count {
  flex-shrink: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--card-color);
  color: #fff;
  font-size: 13px;
  font-weight: 700;
}

.card-skills {
  margin-top: 12px;
  padding-top: 12px;
  border-top: 1px solid var(--wb-line, #d7dbd0);
}

.skill-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 6px 0;
}

.skill-item + .skill-item {
  border-top: 1px dashed var(--wb-line, #d7dbd0);
}

.skill-name {
  font-size: 13px;
  color: var(--wb-ink, #11130e);
  flex: 1;
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.skill-download {
  flex-shrink: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 6px;
  color: var(--wb-muted, #656b60);
  transition: all 0.15s ease;
  text-decoration: none;
}

.skill-download:hover {
  background: var(--card-color);
  color: #fff;
}

/* Transition */
.slide-enter-active,
.slide-leave-active {
  transition: all 0.25s ease;
  overflow: hidden;
}

.slide-enter-from,
.slide-leave-to {
  opacity: 0;
  max-height: 0;
}

.slide-enter-to,
.slide-leave-from {
  opacity: 1;
  max-height: 600px;
}
</style>
