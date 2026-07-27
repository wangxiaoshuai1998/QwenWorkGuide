# Contribution Guide

Thank you for helping improve the WorkBuddy Bluebook. A useful contribution should help readers complete a real task faster and leave behind a method that can be checked, reused, and adapted.

## Good Contributions

- Fix typos, broken links, outdated screenshots, or inaccurate statements.
- Add reproducible cases, troubleshooting notes, and acceptance criteria.
- Share Skills, connectors, API, automation, or multi-agent practices.
- Add role-specific learning paths or industry workflows.
- Improve navigation, search, responsive design, or accessibility.
- Translate pages into English or another language.

## Content Principles

1. **Reproducible**: include the environment, inputs, steps, deliverables, and expected result.
2. **Verifiable**: explain how a reader can confirm the task is actually complete.
3. **Separate facts from experience**: cite product facts and state the scope of personal advice.
4. **Safety first**: explain permissions and risks for files, accounts, credentials, publishing, and external actions.
5. **Respect privacy and copyright**: do not submit personal data, credentials, or material you cannot publish.

## Editing the Book

Each page lives under `docs/bluebook/`:

- `index.md` is the reader-facing page.
- `assets/` contains page images, GIFs, videos, and attachments.
- `source.md`, `source.xml`, and `metadata.json` are local sync artifacts and are not committed by default.

Edit `index.md` for normal content changes. Give new assets meaningful names and reduce file size when possible without hurting readability.

## Validate Locally

```bash
npm install
npm run docs:build
npm run docs:preview
```

Before opening a pull request, confirm that the site builds, internal links work, media loads, desktop and mobile layouts remain readable, and no secrets or generated output are included.

## Pull Requests

Please describe:

- what changed;
- why the change is needed;
- how it was validated;
- whether product facts changed, with sources and a review date when applicable.

Keep each pull request focused on one topic when possible.
