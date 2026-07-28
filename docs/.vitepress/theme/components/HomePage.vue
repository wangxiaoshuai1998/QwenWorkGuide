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
            <span><b>1</b> PART</span>
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
        <a class="wb-reading-card" href="/greenbook/第一篇%20使用手册：先把%20千问办公%20用起来/第1章%20初识%20千问办公/">
          <span class="wb-reading-card__icon"><PixelIcon name="user" /></span>
          <span class="wb-reading-card__content">
            <small>PART 01 · CH. 01</small>
            <strong>初识千问办公：不止对话，更重交付</strong>
            <span>核心能力、与传统 AI 对话的区别，以及典型使用场景。</span>
            <em><b>新手推荐</b><b>五分钟了解</b></em>
          </span>
          <PixelIcon name="arrow-right" class="wb-reading-card__arrow" />
        </a>

        <a class="wb-reading-card" href="/greenbook/第一篇%20使用手册：先把%20千问办公%20用起来/第2章%20Web端使用链路/">
          <span class="wb-reading-card__icon"><PixelIcon name="briefcase" /></span>
          <span class="wb-reading-card__content">
            <small>PART 01 · CH. 02</small>
            <strong>Web 端使用链路：跑通第一个任务</strong>
            <span>登录进入、创建任务、多轮沟通、网盘与网页发布。</span>
            <em><b>浏览器即用</b><b>任务驱动</b></em>
          </span>
          <PixelIcon name="arrow-right" class="wb-reading-card__arrow" />
        </a>

        <a class="wb-reading-card" href="/greenbook/第一篇%20使用手册：先把%20千问办公%20用起来/第3章%20桌面端使用链路/">
          <span class="wb-reading-card__icon"><PixelIcon name="sitemap" /></span>
          <span class="wb-reading-card__content">
            <small>PART 01 · CH. 03</small>
            <strong>桌面端使用链路：从下载到交付</strong>
            <span>下载安装、登录账号、熟悉界面并提交第一个本地任务。</span>
            <em><b>macOS / Windows</b><b>本地执行</b></em>
          </span>
          <PixelIcon name="arrow-right" class="wb-reading-card__arrow" />
        </a>

        <a class="wb-reading-card" href="/greenbook/第一篇%20使用手册：先把%20千问办公%20用起来/第4章%20通用设置/">
          <span class="wb-reading-card__icon"><PixelIcon name="users" /></span>
          <span class="wb-reading-card__content">
            <small>PART 01 · CH. 04</small>
            <strong>通用设置：把账号调到最顺手</strong>
            <span>个人资料、语言与外观、订阅及积分使用管理。</span>
            <em><b>账号管理</b><b>订阅积分</b></em>
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
        <a href="/greenbook/第一篇%20使用手册：先把%20千问办公%20用起来/">
          <PixelIcon name="book" /><strong>本篇导读</strong><span>路线 · 章节 · 总览</span>
        </a>
        <a href="/greenbook/第一篇%20使用手册：先把%20千问办公%20用起来/第1章%20初识%20千问办公/">
          <PixelIcon name="robot" /><strong>认识千问办公</strong><span>能力 · 场景 · 差异</span>
        </a>
        <a href="/greenbook/第一篇%20使用手册：先把%20千问办公%20用起来/第2章%20Web端使用链路/">
          <PixelIcon name="newspaper" /><strong>Web 端上手</strong><span>登录 · 任务 · 发布</span>
        </a>
        <a href="/greenbook/第一篇%20使用手册：先把%20千问办公%20用起来/第3章%20桌面端使用链路/">
          <PixelIcon name="folder-open" /><strong>桌面端上手</strong><span>下载 · 安装 · 交付</span>
        </a>
        <a href="/greenbook/第一篇%20使用手册：先把%20千问办公%20用起来/第4章%20通用设置/">
          <PixelIcon name="check-box" /><strong>通用设置</strong><span>资料 · 外观 · 订阅</span>
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
