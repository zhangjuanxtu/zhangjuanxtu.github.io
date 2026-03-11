# Juan Zhang Academic Homepage

This repository contains the source for Juan Zhang's academic homepage, built with Jekyll and deployed on GitHub Pages.

Live site: https://zhangjuanxtu.github.io/

## Local development

Recommended:

```bash
docker compose up
```

Alternative local build:

```bash
bundle install
bundle exec jekyll serve
```

## Site structure

- `_pages/about.md`: homepage and academic profile
- `_pages/publications.md`: selected publications
- `_pages/teaching.md`: teaching and supervision
- `_pages/honors.md`: honors and awards
- `_bibliography/papers.bib`: publication data

## Deployment

The site is published through GitHub Pages using the workflow in `.github/workflows/deploy.yml`.
