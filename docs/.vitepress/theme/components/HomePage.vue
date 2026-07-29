<script setup lang="ts">
import PixelIcon from "./PixelIcon.vue";
import PixelIconSprite from "./PixelIconSprite.vue";
</script>

<template>
  <main class="wb-home">
    <PixelIconSprite />
    <section class="wb-hero" aria-labelledby="wb-hero-title">
      <div class="wb-hero__stage">
        <div class="wb-hero__copy">
          <p class="wb-pixel-label">OPEN-SOURCE · 4 CHAPTERS · 2026</p>
          <h1 id="wb-hero-title" class="wb-hero__title--greenbook">千问办公绿皮书</h1>
          <p class="wb-hero__summary">
            千问办公——你的全能AI同事，对话即可交付。<br />
            不止于聊天，更懂你的工作。从文档生成到数据分析，从PPT制作到视频剪辑，一句话，AI全流程搞定。
          </p>
          <div class="wb-hero__actions">
            <a class="wb-button wb-button--primary" href="/greenbook/">
              <span>开始阅读</span>
              <PixelIcon name="arrow-right" />
            </a>
            <a class="wb-button wb-button--outline" href="/reading-guide">查看阅读路线</a>
          </div>
        </div>

        <div class="wb-hero__art" aria-label="千问办公像素图标组合">
          <span class="wb-hero__monogram">QW_</span>
          <span class="wb-icon-card wb-icon-card--buddy">
            <PixelIcon name="face-grin" />
          </span>
          <span class="wb-icon-card wb-icon-card--book">
            <PixelIcon name="book" />
          </span>
          <span class="wb-icon-card wb-icon-card--flow">
            <PixelIcon name="sitemap" />
          </span>
          <span class="wb-icon-card wb-icon-card--work">
            <PixelIcon name="briefcase" />
          </span>
          <div class="wb-hero__metrics" aria-label="绿皮书内容规模">
            <span><b>4</b> CHAPTERS</span>
            <span><b>4</b> PARTS</span>
            <span><b>∞</b> WORKFLOWS</span>
          </div>
        </div>
      </div>

      <div class="wb-value-strip" aria-label="绿皮书价值">
        <div class="wb-value-strip__item">
          <PixelIcon name="check-box" />
          <span><b>真实任务</b><small>REAL TASKS</small></span>
        </div>
        <div class="wb-value-strip__item">
          <PixelIcon name="refresh" />
          <span><b>可复现</b><small>REPRODUCIBLE</small></span>
        </div>
        <div class="wb-value-strip__item">
          <PixelIcon name="handshake" />
          <span><b>社区共创</b><small>OPEN SOURCE</small></span>
        </div>
        <div class="wb-value-strip__item">
          <PixelIcon name="grid" />
          <span><b>系统沉淀</b><small>WORK SYSTEM</small></span>
        </div>
      </div>
    </section>

    <section class="wb-section wb-reading" aria-labelledby="wb-reading-title">
      <div class="wb-section__heading">
        <div>
          <p class="wb-pixel-label">READING PATH / 01—04</p>
          <h2 id="wb-reading-title">四段路径，按你的目标进入</h2>
        </div>
        <p>从个人上手到组织落地，循序渐进，构建你的千问办公工作系统。</p>
      </div>

      <div class="wb-reading-grid">
        <a class="wb-reading-card" href="/greenbook/%E7%AC%AC%E4%B8%80%E9%83%A8%E5%88%86%20%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C%EF%BC%9A%E5%85%88%E6%8A%8A%20%E5%8D%83%E9%97%AE%E5%8A%9E%E5%85%AC%20%E7%94%A8%E8%B5%B7%E6%9D%A5/">
          <span class="wb-reading-card__icon"><PixelIcon name="book" /></span>
          <span class="wb-reading-card__content">
            <small>PART 01</small>
            <strong>使用手册：先把千问办公用起来</strong>
            <span>初识千问办公、Web/桌面端使用链路、通用设置、核心功能。</span>
            <em><b>新手推荐</b><b>从零上手</b></em>
          </span>
          <PixelIcon name="arrow-right" class="wb-reading-card__arrow" />
        </a>

        <a class="wb-reading-card" href="/greenbook/%E7%AC%AC%E4%BA%8C%E9%83%A8%E5%88%86%20%E5%AE%9E%E6%88%98%E6%A1%88%E4%BE%8B%20%E4%BB%8E%E5%85%B7%E4%BD%93%E4%BB%BB%E5%8A%A1%EF%BC%8C%E8%B5%B0%E5%90%91AI%20Native/">
          <span class="wb-reading-card__icon"><PixelIcon name="briefcase" /></span>
          <span class="wb-reading-card__content">
            <small>PART 02</small>
            <strong>实战案例：从具体任务，走向AI Native</strong>
            <span>电商数据大屏、声音克隆、文档写作、数据分析等真实场景。</span>
            <em><b>任务驱动</b><b>即学即用</b></em>
          </span>
          <PixelIcon name="arrow-right" class="wb-reading-card__arrow" />
        </a>

        <a class="wb-reading-card" href="/greenbook/%E7%AC%AC%E4%B8%89%E9%83%A8%E5%88%86%20%E8%BF%9B%E9%98%B6%E4%BD%BF%E7%94%A8%E6%A1%88%E4%BE%8B/">
          <span class="wb-reading-card__icon"><PixelIcon name="sitemap" /></span>
          <span class="wb-reading-card__content">
            <small>PART 03</small>
            <strong>进阶使用案例：深入场景实战</strong>
            <span>公众号排版、UI 到前端原型、需求生成原型图、图片设计。</span>
            <em><b>进阶实战</b><b>场景深入</b></em>
          </span>
          <PixelIcon name="arrow-right" class="wb-reading-card__arrow" />
        </a>

        <a class="wb-reading-card" href="/greenbook/%E7%AC%AC%E5%9B%9B%E9%83%A8%E5%88%86%20%E8%AE%A4%E7%9F%A5%E4%B8%8E%E6%96%B9%E6%B3%95%E8%AE%BA/">
          <span class="wb-reading-card__icon"><PixelIcon name="users" /></span>
          <span class="wb-reading-card__content">
            <small>PART 04</small>
            <strong>认知与方法论：构建AI工作系统</strong>
            <span>AI 工作流方法论、Skill 编写详解、IP 配图与排版 Skill 架构。</span>
            <em><b>方法论</b><b>Skill 开发</b></em>
          </span>
          <PixelIcon name="arrow-right" class="wb-reading-card__arrow" />
        </a>
      </div>
    </section>

    <section class="wb-section wb-task-index" aria-labelledby="wb-task-index-title">
      <div class="wb-section__heading wb-section__heading--compact">
        <div>
          <p class="wb-pixel-label">START WITH A REAL TASK</p>
          <h2 id="wb-task-index-title">你现在想让 AI 帮你做什么？</h2>
        </div>
        <p>不必从头读。带着问题进来，先跑通一个能验收的结果。</p>
      </div>

      <div class="wb-task-grid">
        <a href="/greenbook/%E7%AC%AC%E4%BA%8C%E9%83%A8%E5%88%86%20%E5%AE%9E%E6%88%98%E6%A1%88%E4%BE%8B%20%E4%BB%8E%E5%85%B7%E4%BD%93%E4%BB%BB%E5%8A%A1%EF%BC%8C%E8%B5%B0%E5%90%91AI%20Native/%E5%AE%9E%E6%88%98%E6%8C%87%E5%8D%97%EF%BD%9CExcel%20%E8%A1%A8%E6%A0%BC%E6%95%B0%E6%8D%AE%E5%A4%84%E7%90%86/">
          <PixelIcon name="chart-line" /><strong>数据分析</strong><span>Excel · 数据分析全流程</span>
        </a>
        <a href="/greenbook/%E7%AC%AC%E4%BA%8C%E9%83%A8%E5%88%86%20%E5%AE%9E%E6%88%98%E6%A1%88%E4%BE%8B%20%E4%BB%8E%E5%85%B7%E4%BD%93%E4%BB%BB%E5%8A%A1%EF%BC%8C%E8%B5%B0%E5%90%91AI%20Native/%E8%87%AA%E5%AA%92%E4%BD%93-%E4%B8%8A%E4%BC%A0%E5%BD%95%E9%9F%B3%EF%BC%8C%E5%85%8B%E9%9A%86%E8%87%AA%E5%B7%B1%E7%9A%84%E5%A3%B0%E9%9F%B3%E5%81%9A%E5%8F%A3%E6%92%AD/">
          <PixelIcon name="video-camera" /><strong>内容创作</strong><span>公众号排版 · 声音克隆 · 视频</span>
        </a>
        <a href="/greenbook/%E7%AC%AC%E4%BA%8C%E9%83%A8%E5%88%86%20%E5%AE%9E%E6%88%98%E6%A1%88%E4%BE%8B%20%E4%BB%8E%E5%85%B7%E4%BD%93%E4%BB%BB%E5%8A%A1%EF%BC%8C%E8%B5%B0%E5%90%91AI%20Native/%E5%AE%9E%E6%88%98%E6%8C%87%E5%8D%97%EF%BD%9C4%E4%B8%AA%E5%9C%BA%E6%99%AF%E6%95%99%E4%BD%A0%E7%94%A8%20%E5%8D%83%E9%97%AE%E5%8A%9E%E5%85%AC%20%E5%91%8A%E5%88%AB%E9%87%8D%E5%A4%8D%E5%B7%A5%E4%BD%9C/">
          <PixelIcon name="check-box" /><strong>办公效率</strong><span>告别重复 · 场景实战</span>
        </a>
        <a href="/greenbook/%E7%AC%AC%E4%B8%89%E9%83%A8%E5%88%86%20%E8%BF%9B%E9%98%B6%E4%BD%BF%E7%94%A8%E6%A1%88%E4%BE%8B/%E5%AE%9E%E6%88%98%E6%8C%87%E5%8D%97%EF%BD%9C%E7%94%B1%E9%9C%80%E6%B1%82%E7%9B%B4%E6%8E%A5%E7%94%9F%E6%88%90%E5%8E%9F%E5%9E%8B%E5%9B%BE/">
          <PixelIcon name="grid" /><strong>开发辅助</strong><span>UI 到原型 · 需求到原型图</span>
        </a>
        <a href="/greenbook/%E7%AC%AC%E5%9B%9B%E9%83%A8%E5%88%86%20%E8%AE%A4%E7%9F%A5%E4%B8%8E%E6%96%B9%E6%B3%95%E8%AE%BA/%E6%80%8E%E4%B9%88%E5%86%99%E5%87%BA%E4%B8%80%E4%B8%AAskill/">
          <PixelIcon name="robot" /><strong>AI 工作流</strong><span>Skill 编写 · 方法论</span>
        </a>
      </div>
    </section>

    <section class="wb-section wb-system" aria-labelledby="wb-system-title">
      <div class="wb-system__intro">
        <p class="wb-pixel-label">FROM TASK TO TEAM</p>
        <h2 id="wb-system-title">一次成功，不该只发生一次。</h2>
        <p>绿皮书真正关心的不是“AI 会什么”，而是如何把一个结果沉淀成稳定、可协作、可复用的工作系统。</p>
      </div>
      <ol class="wb-system__steps">
        <li><b>01</b><strong>TASK</strong><span>完成一个真实任务</span></li>
        <li><b>02</b><strong>CASE</strong><span>复盘成可复现案例</span></li>
        <li><b>03</b><strong>WORKFLOW</strong><span>沉淀 Skill 与自动化</span></li>
        <li><b>04</b><strong>AI TEAM</strong><span>组合成协作团队</span></li>
      </ol>
    </section>

    <section class="wb-community" aria-labelledby="wb-community-title">
      <div>
        <p class="wb-pixel-label">BUILD IN PUBLIC · LEARN IN PUBLIC</p>
        <h2 id="wb-community-title">这本绿皮书，也可以由你继续写下去。</h2>
      </div>
      <div class="wb-community__actions">
        <a class="wb-button wb-button--acid" href="/community/contributing">参与共创</a>
        <a class="wb-button wb-button--dark-outline" href="https://github.com/wangxiaoshuai1998/QwenWorkGuide">前往 GitHub</a>
      </div>
      <PixelIcon name="book" class="wb-community__icon" />
    </section>
  </main>
</template>
