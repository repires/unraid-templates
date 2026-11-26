<p align="center">
  <img src="icon.svg" alt="Unraid Templates by repires" width="80" height="80">
</p>

<h1 align="center">Unraid Templates</h1>

<p align="center">
  <a href="https://github.com/repires/unraid-templates/actions"><img src="https://img.shields.io/github/actions/workflow/status/repires/unraid-templates/nod-images.yml?branch=main&label=Builds&style=for-the-badge&logo=githubactions&logoColor=white" alt="Builds" height="32"></a>&nbsp;
  <a href="#templates"><img src="https://img.shields.io/badge/Templates-16-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Templates" height="32"></a>&nbsp;
  <a href="https://github.com/repires/unraid-templates/commits/main"><img src="https://img.shields.io/github/last-commit/repires/unraid-templates?branch=main&style=for-the-badge&logo=git&logoColor=white&label=Updated" alt="Last commit" height="32"></a>&nbsp;
  <a href="https://unraid.net"><img src="https://img.shields.io/badge/Unraid-Community%20Apps-f15a2c?style=for-the-badge&logo=unraid&logoColor=white" alt="Unraid" height="32"></a>&nbsp;
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License" height="32"></a>
</p>

<p align="center">
  Docker XML templates for Unraid, published in Community Applications as <b>pires' Repository</b>.<br>
  Maintained for modern AI workflows, media tools, and self-hosted services.
</p>

---

## Templates

### AI & Agents

<img src="https://raw.githubusercontent.com/akitaonrails/ai-memory/v3.4.7/companions/ai-memory-desktop/icons/icon.png" width="72" align="left" alt="ai-memory">
<a href="https://github.com/akitaonrails/ai-memory#readme"><img src="https://img.shields.io/badge/Repository-393939?style=for-the-badge&logo=github&logoColor=white" align="right" alt="Repository"></a>
<a href="templates/ai-memory.xml"><img src="https://img.shields.io/badge/XML%20Template-2496ED?style=for-the-badge&logo=docker&logoColor=white" align="right" alt="XML Template"></a>

**ai-memory**<br>
Persistent, shared memory for AI coding agents over MCP: session capture, a searchable wiki, and handoffs between agents. Runs upstream `akitaonrails/ai-memory:latest`.

<br clear="all">

<img src="https://raw.githubusercontent.com/milind-soni/OpenMausBot/v0.1.169/public/app-icon-512.png" width="72" align="left" alt="OpenMausBot">
<a href="https://github.com/milind-soni/OpenMausBot#readme"><img src="https://img.shields.io/badge/Repository-393939?style=for-the-badge&logo=github&logoColor=white" align="right" alt="Repository"></a>
<a href="templates/openmausbot.xml"><img src="https://img.shields.io/badge/XML%20Template-2496ED?style=for-the-badge&logo=docker&logoColor=white" align="right" alt="XML Template"></a>

**OpenMausBot**<br>
Open-source workspace for AI bots: chat with bots that run Claude Code, Codex, OpenCode and other engines, each with its own shell, files, and browser. Runs upstream `ghcr.io/milind-soni/openmausbot:latest`.

<br clear="all">

<img src="icons/rakazo.png" width="72" align="left" alt="Rakazo">
<a href="https://rakazo.com"><img src="https://img.shields.io/badge/Website-393939?style=for-the-badge&logo=googlechrome&logoColor=white" align="right" alt="Website"></a>
<a href="templates/rakazo-web.xml"><img src="https://img.shields.io/badge/4%20Templates-2496ED?style=for-the-badge&logo=docker&logoColor=white" align="right" alt="XML Templates"></a>

**Rakazo**<br>
Open-source Grok Bot alternative with persistent AI teammates, memory, routines, and Docker computers. Packaged as 4 coordinated templates: `rakazo-postgres`, `rakazo-supervisor`, `rakazo-api`, and `rakazo-web`.

<br clear="all">

<img src="https://raw.githubusercontent.com/n8n-io/nod/nod-v0.8.4/public/nod-logo.png" width="72" align="left" alt="Nod">
<a href="https://nod.n8n.io"><img src="https://img.shields.io/badge/Website-393939?style=for-the-badge&logo=googlechrome&logoColor=white" align="right" alt="Website"></a>
<a href="templates/nod-server.xml"><img src="https://img.shields.io/badge/6%20Templates-2496ED?style=for-the-badge&logo=docker&logoColor=white" align="right" alt="XML Templates"></a>

**Nod**<br>
Self-hosted personal AI assistant from the n8n team. Packaged as 6 templates with secure network isolation and custom-built GHCR images: `nod-postgres`, `nod-runtime`, `nod-browser-unraid`, `nod-workspace-network`, `nod-workspace-unraid`, and `nod-server`.

<br clear="all">

---

### Media & Automation

<img src="icons/immich-photo-manager.png" width="72" align="left" alt="immich-photo-manager">
<a href="https://github.com/drolosoft/immich-photo-manager#readme"><img src="https://img.shields.io/badge/Repository-393939?style=for-the-badge&logo=github&logoColor=white" align="right" alt="Repository"></a>
<a href="templates/immich-photo-manager.xml"><img src="https://img.shields.io/badge/XML%20Template-2496ED?style=for-the-badge&logo=docker&logoColor=white" align="right" alt="XML Template"></a>

**immich-photo-manager**<br>
Model Context Protocol (MCP) server bringing rich Immich photo library management, search, album creation, person/face querying, and PDF/archive exporting to AI agents over HTTP.

<br clear="all">

<img src="icons/immich-autotag.png" width="72" align="left" alt="immich-autotag">
<a href="https://github.com/txemi/immich-autotag#readme"><img src="https://img.shields.io/badge/Repository-393939?style=for-the-badge&logo=github&logoColor=white" align="right" alt="Repository"></a>
<a href="templates/immich-autotag.xml"><img src="https://img.shields.io/badge/XML%20Template-2496ED?style=for-the-badge&logo=docker&logoColor=white" align="right" alt="XML Template"></a>

**immich-autotag**<br>
Automated rule engine for Immich that batch-processes photo and video libraries: applies smart tags and albums, corrects dates, manages permissions, and schedules runs via cron.

<br clear="all">

---

### Network & Utilities

<img src="icons/error-pages.svg" width="72" align="left" alt="error-pages">
<a href="https://github.com/tarampampam/error-pages#readme"><img src="https://img.shields.io/badge/Repository-393939?style=for-the-badge&logo=github&logoColor=white" align="right" alt="Repository"></a>
<a href="templates/error-pages.xml"><img src="https://img.shields.io/badge/XML%20Template-2496ED?style=for-the-badge&logo=docker&logoColor=white" align="right" alt="XML Template"></a>

**error-pages**<br>
Lightweight, fast, and responsive HTTP error pages with 50+ built-in themes for Traefik, Nginx, HAProxy, and Caddy.

<br clear="all">

<img src="https://raw.githubusercontent.com/Zarestia-Dev/rclone-manager/v0.3.6/backend/desktop/icons/icon.png" width="72" align="left" alt="RClone Manager">
<a href="https://github.com/Zarestia-Dev/rclone-manager#readme"><img src="https://img.shields.io/badge/Repository-393939?style=for-the-badge&logo=github&logoColor=white" align="right" alt="Repository"></a>
<a href="templates/rclone-manager.xml"><img src="https://img.shields.io/badge/XML%20Template-2496ED?style=for-the-badge&logo=docker&logoColor=white" align="right" alt="XML Template"></a>

**RClone Manager**<br>
Modern web-based GUI for managing rclone remotes, transfers, file browsing, and automated synchronization tasks.

<br clear="all">

---

## Install

### Via Community Applications (Recommended)
1. Open the **Apps** tab on your Unraid server.
2. Search for any template name (e.g., `ai-memory`, `openmausbot`, `nod`, `immich-photo-manager`).
3. Click **Install**.

### Manual Template Install
To add a template directly without CA, paste its raw XML URL into **Docker → Add Container → Template**:
```text
https://raw.githubusercontent.com/repires/unraid-templates/main/templates/ai-memory.xml
```

---

## App Setup & Highlights

<details>
<summary><b>ai-memory Setup Details</b></summary>

1. Set **Auth token** (e.g. `openssl rand -hex 32`).
2. Add your server hostnames and IPs to **Allowed hosts** (e.g. `localhost,127.0.0.1,192.168.1.10,tower.local`).
3. Connect MCP clients at `http://<server>:49374/mcp` with header `Authorization: Bearer <token>`.
4. Web console (`/web`) requires HTTPS behind a reverse proxy with **Secure cookie** enabled.
</details>

<details>
<summary><b>OpenMausBot Setup Details</b></summary>

1. Set **Public URL** to your access address (LAN IP or reverse proxy).
2. Run `docker exec openmausbot openmausbot pair` in the Unraid terminal to link your browser or app.
3. Install and configure engines under **Settings → Engines**.
</details>

<details>
<summary><b>Rakazo Stack Setup Details</b></summary>

Requires the `rakazo` Docker network (`docker network create rakazo`). Install the four templates in order:
1. `rakazo-postgres`
2. `rakazo-supervisor`
3. `rakazo-api`
4. `rakazo-web`
Access the interface on port `3000`.
</details>

<details>
<summary><b>Nod Stack Setup Details</b></summary>

Packaged across 6 containers with custom images (`ghcr.io/repires/nod-*`):
1. `nod-postgres` (Database)
2. `nod-runtime` (Docker gateway)
3. `nod-browser-unraid` (Headless browser)
4. `nod-workspace-network` (Workspace firewall)
5. `nod-workspace-unraid` (Execution sandbox)
6. `nod-server` (Application web interface)
</details>

---

## Maintenance & Builds

- **Upstream Images**: Templates for `ai-memory`, `openmausbot`, `error-pages`, `rclone-manager`, `rakazo`, `immich-photo-manager`, and `immich-autotag` track upstream release tags so Unraid's Docker update advisor notifies you of new releases immediately.
- **Nod Automated Builds**: [`nod-images.yml`](.github/workflows/nod-images.yml) monitors upstream releases daily and rebuilds images weekly so Debian/Node security patches remain fresh.
- **Upstream Watcher**: [`upstream-watch.yml`](.github/workflows/upstream-watch.yml) tracks changes in upstream Dockerfiles and dependencies via [`.github/upstream-watch.json`](.github/upstream-watch.json), automatically flagging any breaking upstream adjustments.

---

## Support & Issues

- For template, configuration, or packaging issues, please open an issue in this repository: [repires/unraid-templates/issues](https://github.com/repires/unraid-templates/issues).
- For upstream bugs in the applications themselves, please consult their respective upstream issue trackers.

---

## License

This repository and its templates are licensed under the [MIT License](LICENSE). Third-party applications retain their respective upstream licenses.
