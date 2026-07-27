<p align="center">
  <a href="https://qwenwork.ink/">
    <img src="./assets/workbuddy-guide-banner.png" alt="QwenWork Guide homepage preview" width="100%">
  </a>
</p>

<h1 align="center">QwenWork Guide (QwenWork Greenbook)</h1>

<p align="center"><strong>A hands-on Chinese user manual for QwenWork</strong></p>

<p align="center">
  English · <a href="./README.md">简体中文</a> ·
  <a href="https://qwenwork.ink/">Read Online</a> ·
  <a href="./docs/reading-guide.md">Reading Guide</a> ·
  <a href="./CONTRIBUTING_en.md">Contribute</a>
</p>

> This is a task-driven field guide, not a rewritten feature manual. The current release covers Part I · User Manual (part introduction + Chapters 1–4): getting to know QwenWork, the web workflow, the desktop workflow, and general settings. More parts will be published continuously.

## Background / Upstream

This project originates from the open-source WorkBuddy Bluebook ([AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)) and has been rebuilt on top of its site framework as the QwenWork Guide. The book content is exported from a DingTalk knowledge base and maintained around real QwenWork workflows.

## Read Online

The recommended reading experience is **[qwenwork.ink](https://qwenwork.ink/)**. The website provides full navigation, local search, page outlines, dark mode, rendered diagrams, and mobile support.

The book is currently written primarily in Simplified Chinese. English contributions and translation proposals are welcome.

## What Is Inside

Currently available: **Part I · User Manual (part introduction + Chapters 1–4)**. More parts are on the way.

| Chapter | Topics |
| --- | --- |
| Part Introduction | Reading paths, chapter overview, and learning goals |
| Ch. 1 Getting to Know QwenWork | Core capabilities, differences from plain AI chat, and typical scenarios |
| Ch. 2 Web Workflow | Signing in, creating tasks, multi-turn collaboration, cloud drive, and web publishing |
| Ch. 3 Desktop Workflow | Download, installation, sign-in, interface tour, and the first local task |
| Ch. 4 General Settings | Profile, language and appearance, subscription, and credit management |

## How to Read

- **New to QwenWork**: start with Chapter 1 and complete Part I in order.
- **Want to get hands-on quickly**: jump to Chapter 2 (web) or Chapter 3 (desktop), finish a first task, then fill in the rest.
- **Looking for more**: future parts (cases, advanced topics) will be published continuously—watch this repository for updates.

## Local Development

Node.js 20–24 is supported; Node.js 22 is recommended.

```bash
npm install
npm run dev
```

Build and preview the static site:

```bash
npm run docs:build
npm run docs:preview
```

## Contributing

Contributions are welcome, including:

- corrections for typos, broken links, and outdated information;
- reproducible real-world QwenWork cases;
- Skills, connectors, API, and automation practices;
- role-specific and industry-specific workflows;
- improvements to navigation, search, design, and accessibility;
- English translations.

Read the [Contribution Guide](./CONTRIBUTING_en.md) or open an [Issue](https://github.com/AlephAITech/WorkBuddyGuide/issues).

## Deployment

The site uses **VitePress + Cloudflare Pages + GitHub**. Cloudflare Pages builds and deploys the `main` branch automatically. See [DEPLOYMENT.md](./DEPLOYMENT.md) for the exact settings.

## Authors

Thanks to the authors who created and maintain the upstream WorkBuddy Bluebook ([AlephAITech/WorkBuddyGuide](https://github.com/AlephAITech/WorkBuddyGuide)). Click a card to view the full-size image and scan its QR code.

<p align="center">
  <a href="./assets/authors/jia-mu-wei-lai-pai.png"><img src="./assets/authors/jia-mu-wei-lai-pai.png" alt="甲木未来派" width="48%"></a>
  <a href="./assets/authors/mo-yu-xiao-li.png"><img src="./assets/authors/mo-yu-xiao-li.png" alt="摸鱼小李" width="48%"></a>
</p>

<p align="center">
  <a href="./assets/authors/dai-shu-di-ai-ke-zhan.png"><img src="./assets/authors/dai-shu-di-ai-ke-zhan.png" alt="袋鼠帝AI客栈" width="48%"></a>
  <a href="./assets/authors/liu-cong-nlp.png"><img src="./assets/authors/liu-cong-nlp.png" alt="刘聪NLP" width="48%"></a>
</p>

<p align="center">
  <a href="./assets/authors/cang-he.png"><img src="./assets/authors/cang-he.png" alt="苍何" width="48%"></a>
</p>

## Disclaimer

This is a community-maintained QwenWork practice guide. For time-sensitive product details—including features, UI, pricing, availability, and security policies—refer to official QwenWork sources.

## License

This project is licensed under the [MIT License](./LICENSE). You may use, copy, modify, and distribute it, provided that the original copyright notice and license text are retained.
