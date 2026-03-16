# 个人介绍博客一键部署开发文档（给 AI 直接执行）

## 1. 目标与范围

目标：让另一个人把本仓库快速部署成可用的学术个人主页，并可持续更新。

本项目基于 al-folio（Jekyll）实现，已包含以下定制方向：
- 首页简洁化（About 页）
- 详细履历放在 CV 页
- Publications 作为论文全集入口
- Talks 与 Activities 分离管理
- 首页 News 展示动态与活动
- 顶部导航快速入口（邮箱、Google Scholar）

适用对象：
- 接手维护本网站的人
- 需要把本文档直接发给 AI 执行的人

## 2. 关键约束（必须遵守）

### 2.1 技术与构建约束
- 优先使用 Docker 本地预览。
- 生产发布走 GitHub Actions + GitHub Pages。
- 页面与内容文件使用 Markdown + YAML frontmatter。
- 保持现有 al-folio 结构，不擅自重构主题核心。

### 2.2 内容与风格约束
- 首页使用第一人称（I / My），避免第三人称叙述。
- 首页以简洁为主，不重复展示 Publications 细节。
- Research / Education / Appointments / Selected Roles 放在 CV 页。
- News 必须可读，禁止出现只有日期无内容的空行。
- 新增活动优先写入 Activities 页，并同步为可选 News 条目。

### 2.3 YAML 约束（高优先级）
- frontmatter 中如果字段值包含英文冒号 :，必须加双引号。
- 示例：
  - 正确：title: "Website Update: A Simpler Homepage"
  - 错误：title: Website Update: A Simpler Homepage
- 该规则直接影响 Jekyll 解析，错误会导致 News 异常（如空白条目）。

### 2.4 Git 约束
- 只提交与本次需求相关的文件。
- 不要把无关临时文件、脚本、素材目录一起提交。
- 每次改动后先检查状态再 commit。

## 3. 目录与文件职责

核心文件：
- 首页内容：[ _pages/about.md ](_pages/about.md)
- 新闻列表渲染模板：[ _includes/news.liquid ](_includes/news.liquid)
- 首页布局模板：[ _layouts/about.liquid ](_layouts/about.liquid)
- 履历页：[ _pages/cv.md ](_pages/cv.md)
- 论文页：[ _pages/publications.md ](_pages/publications.md)
- 学术报告页：[ _pages/talks.md ](_pages/talks.md)
- 活动页：[ _pages/activities.md ](_pages/activities.md)
- 新闻条目目录：[ _news ](_news)
- 站点总配置：[ _config.yml ](_config.yml)

## 4. 一键部署流程（人工可执行）

### 4.1 获取代码
~~~bash
git clone https://github.com/<your-account>/<your-repo>.git
cd <your-repo>
~~~

### 4.2 校验仓库命名与站点地址
- 用户主页仓库应命名为 <github-username>.github.io。
- 确认 [ _config.yml ](_config.yml) 中：
  - url 为 https://<github-username>.github.io
  - baseurl 为空（个人主页场景）

### 4.3 本地预览（推荐 Docker）
~~~bash
docker compose pull
docker compose up --build
~~~
浏览器访问：http://localhost:8080

### 4.4 代码格式化（提交前）
~~~bash
npm install --save-dev prettier @shopify/prettier-plugin-liquid
npx prettier . --write
~~~

### 4.5 提交与发布
~~~bash
git add <changed-files>
git commit -m "Update personal homepage content and layout"
git push
~~~

### 4.6 GitHub Pages 设置
- Settings -> Pages -> Source 选择 GitHub Actions。
- Actions 允许 workflow 写权限。

## 5. 内容更新 SOP（接手者常用）

### 5.1 更新首页简介
编辑 [ _pages/about.md ](_pages/about.md)：
- 保留简洁简介
- 保留 Quick Navigation
- 保留 Student Recruitment

### 5.2 新增新闻
在 [ _news ](_news) 下新建文件，例如：
~~~text
YYYY-MM-DD-short-title.md
~~~

模板：
~~~yaml
---
layout: post
date: 2026-03-16
title: "News Title with Optional: Colon"
inline: true
related_posts: false
---
One sentence summary. [Details](https://example.com).
~~~

### 5.3 新增活动
- 先更新 [ _pages/activities.md ](_pages/activities.md) 的活动列表。
- 再按需新增一条 _news 条目，将活动同步到首页动态。

### 5.4 新增报告/会议
更新 [ _pages/talks.md ](_pages/talks.md)：
- 英文表达
- 时间、地点、报告标题结构一致
- 风格与现有 list-group 保持一致

## 6. 验收清单（必须全部通过）

- 首页头像尺寸协调，不遮挡正文。
- 首页为第一人称表达。
- 首页存在可读 News，且无空白行。
- Publications 不在首页重复大段展示。
- CV 页面包含完整履历板块。
- Talks 与 Activities 可从导航进入。
- 深色模式下文字可读。
- 推送后 GitHub Actions 构建成功。

## 7. 故障排查速查表

### 7.1 News 出现“只有日期，没有内容”
优先检查：
- 对应 _news 文件 frontmatter 是否 YAML 语法错误。
- title 含冒号是否加了双引号。
- 新闻模板 [ _includes/news.liquid ](_includes/news.liquid) 是否被误改。

### 7.2 样式在深色模式不可读
检查：
- 是否使用了硬编码白色背景或黑色文字。
- 优先使用主题变量：
  - var(--global-text-color)
  - var(--global-bg-color)
  - var(--global-divider-color)

### 7.3 页面不显示在导航
检查 frontmatter：
- nav: true
- published: true
- nav_order 是否合理

## 8. 可直接发给 AI 的一键执行提示词

将以下内容原样发给 AI（把尖括号参数替换掉）：

---
你现在是本仓库的实施工程师，请在不改动无关文件的前提下，完成个人介绍博客部署与初始化。

仓库信息：
- 仓库地址：<repo-url>
- 目标域名：https://<github-username>.github.io
- 技术栈：Jekyll + al-folio + GitHub Pages

强约束：
1) 只修改以下范围：_pages, _news, _includes/news.liquid, _layouts/about.liquid, _config.yml, _data/socials.yml。
2) 首页 about 使用第一人称，保持简洁，不重复展示 publications 明细。
3) 详细履历放到 CV 页，包含 Research/Education/Appointments/Selected Roles。
4) News 必须可读，禁止空白条目。
5) _news frontmatter 若 title 含冒号必须加双引号。
6) 新增活动写入 Activities 页，并可选同步为 News。
7) 深色模式可读，不允许硬编码白底白字冲突。
8) 提交前执行格式化；仅提交本次相关文件。

执行步骤：
- 校验并更新 _config.yml 中 url/baseurl。
- 校验导航与页面存在：About/CV/Publications/Talks/Activities/News。
- 按以上约束更新页面与新闻内容。
- 运行本地构建（优先 docker compose up --build）。
- 输出变更文件清单、关键 diff 摘要、部署后访问链接。
- 最后执行 git add + git commit + git push。

验收输出：
- 列出首页、CV、Talks、Activities、News 的最终入口地址。
- 说明如何继续新增一条活动与一条新闻。
---

## 9. 交付建议

建议在每次大改后新增 CHANGELOG 条目，记录：
- 修改日期
- 修改人
- 影响页面
- 风险点
- 回滚方式
