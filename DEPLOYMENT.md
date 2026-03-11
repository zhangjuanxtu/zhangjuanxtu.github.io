# Deployment Notes

This repository has been converted to an al-folio based Jekyll academic homepage.

## Repository Naming

For a GitHub user site, the repository must be renamed to `<github-username>.github.io`.

The current site configuration in `_config.yml` assumes the final site URL will be:

- `https://zhangjuanxtu.github.io/`

For this account, the target repository name should be:

- `zhangjuanxtu.github.io`

## GitHub Settings

1. Rename the repository from `zhangjuan` to `zhangjuanxtu.github.io`.
2. If the remote URL changes after the rename, update the local remote:
   `git remote set-url origin https://github.com/zhangjuanxtu/zhangjuanxtu.github.io.git`
3. In GitHub repository settings, open the Pages section.
4. Set the publishing source to `GitHub Actions`.
5. In GitHub Actions settings, make sure workflows have permission to write repository contents.
6. The old `gh-pages` branch is no longer the publishing source for this setup. If it still exists, it can be ignored once Pages is switched to `GitHub Actions`.

## Local Preview

Two preview paths are available:

- Ruby/Bundler: `bundle exec jekyll build` or `bundle exec jekyll serve`
- Docker: `docker compose up --build`

In the current local environment, Bundler is not installed and Docker daemon access is not available to the current user, so deployment readiness was verified at the configuration level rather than by a full local preview build.