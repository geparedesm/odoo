# AGENTS.md

## Project Overview

This repository contains an Odoo 13 setup with a custom website addon located at `odoo/addons/custom_web`.

The addon powers a portfolio site and includes:
- public website templates
- custom frontend assets
- backend portfolio content models
- an Odoo administration screen under `Portfolio -> Content`

## Important Paths

- Dev compose: `docker-compose.dev.yaml`
- Prod compose: `docker-compose.yaml`
- Odoo config: `odoo/etc/odoo.conf`
- Custom addon: `odoo/addons/custom_web`
- Website templates: `odoo/addons/custom_web/views/templates.xml`
- Backend views: `odoo/addons/custom_web/views/views.xml`
- Frontend CSS: `odoo/addons/custom_web/static/src/css/main.css`
- Frontend JS: `odoo/addons/custom_web/static/src/js/main.js`
- Seeded content: `odoo/addons/custom_web/data/portfolio_data.xml`

## Local Development

Use the development stack, not the production compose file.

Start:

```bash
docker compose -f docker-compose.dev.yaml up -d
```

Stop:

```bash
docker compose -f docker-compose.dev.yaml down
```

Odoo runs at:

```text
http://localhost:8069
```

## Module Refresh

When changing addon models, views, templates, or assets, upgrade the module:

```bash
docker compose -f docker-compose.dev.yaml exec odoo \
  odoo -c /etc/odoo/odoo.conf -d admin -u custom_web --stop-after-init
```

The main dev database currently used here is:

```text
admin
```

## Portfolio Admin

The portfolio content is managed in Odoo backend:

```text
/web -> Portfolio -> Content
```

Do not hardcode portfolio content in templates unless intentionally creating a fallback.

## Working Rules

- Prefer `docker-compose.dev.yaml` for all local work.
- Treat `docker-compose.yaml` as production-oriented.
- Do not remove or overwrite user changes outside the requested task.
- Use `apply_patch` for manual file edits.
- After changing XML, CSS, JS, models, or manifest data, upgrade `custom_web`.
- If frontend changes do not appear, assume Odoo asset caching first and reload the module.
- Keep changes scoped to the custom addon unless the task clearly requires wider repo changes.

## Custom Web Notes

- The portfolio homepage is served from `/`.
- The site uses `website.layout`.
- The default Odoo footer is intentionally hidden on the portfolio page.
- Sidebar and hero are heavily customized in the addon templates and CSS.
- Portfolio records are stored in custom models such as `portfolio.profile`, `portfolio.project`, and related content models.

## Verification

Useful checks:

```bash
docker compose -f docker-compose.dev.yaml ps
docker compose -f docker-compose.dev.yaml logs --tail=200 odoo
docker exec odoo-odoo-1 curl -I http://127.0.0.1:8069/
```

## Safe Assumptions

- Odoo version is 13.0
- Postgres runs in Docker
- The custom addon is mounted through `/mnt/extra-addons`
- The user is actively editing the portfolio UX and admin content flow
