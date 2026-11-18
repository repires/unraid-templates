# Unraid templates by repires

Docker templates for Unraid, published in Community Applications as **pires' Repository**.
Install them from the **Apps** tab by searching for the app name. Each template's `TemplateURL`
points at its XML in this repository, so template fixes reach installed apps.

| App | Templates | Images |
|---|---|---|
| [ai-memory](#ai-memory) | `ai-memory` | upstream `akitaonrails/ai-memory` |
| [OpenMausBot](#openmausbot) | `openmausbot` | upstream `ghcr.io/milind-soni/openmausbot` |
| [error-pages](#error-pages) | `error-pages` | upstream `tarampampam/error-pages` |
| [Nod](#nod) | six `nod-*` templates | `ghcr.io/repires/nod-*`, built here from upstream releases |

Tested on Unraid 7.3 with Docker 29.

## ai-memory

[ai-memory](https://github.com/akitaonrails/ai-memory) (MIT, by Fabio Akita) gives AI coding agents
persistent, shared memory over MCP: session capture, a searchable wiki and handoffs between agents.
It is a single container with a SQLite database. The template runs the upstream image
`akitaonrails/ai-memory:latest` as published; nothing is rebuilt here.

1. Set **Auth token**, for example from `openssl rand -hex 32`. It is required because without
   a token ai-memory accepts every request.
2. Add every hostname and IP your clients use to reach the server to **Allowed hosts**, for example
   `localhost,127.0.0.1,192.168.1.10,tower.local`. Requests with any other `Host` header are refused.
3. Point MCP clients at `http://<server>:49374/mcp` with `Authorization: Bearer <token>`. With the
   ai-memory CLI on the client machine, `ai-memory install-mcp --client <name> --auth-token <token>`
   writes the client config.
4. LLM and embedding providers are optional (Advanced view). Without them ai-memory uses
   full-text search and rule-based summaries.

Notes:

- The container runs as `99:100` (nobody:users), which owns the appdata folders Unraid creates,
  so no permission changes are needed.
- On plain HTTP the bearer token travels unencrypted, and ai-memory logs a warning about it. Use
  a reverse proxy with HTTPS if clients connect over an untrusted network.
- The web console (`/web`) needs HTTPS. Put ai-memory behind a reverse proxy, then set
  **Secure cookie** to `true`, a **Root username** and an **Initial root password**. Clear the
  password after the first start. **Don't set a root password on plain HTTP:** ai-memory then
  refuses to start, and keeps refusing until Secure cookie is enabled behind HTTPS.

## OpenMausBot

[OpenMausBot](https://github.com/milind-soni/OpenMausBot) (Apache-2.0, by Milind Soni) is an
open-source workspace for AI bots: chat with bots that run Claude Code, Codex, OpenCode and other
engines, each with its own shell, files and browser. The template runs the project's official
server image `ghcr.io/milind-soni/openmausbot:latest` as published.

1. Set **Public URL** to the address devices will use, for example `http://192.168.1.10:8799`,
   or an `https://` address from Tailscale Serve or a reverse proxy.
2. Pair your first browser: in the Unraid terminal run `docker exec openmausbot openmausbot pair`
   and open the printed link (or paste it into the desktop app, or scan the QR code with a phone).
   Every device pairs once.
3. Install engines from **Settings → Engines** and sign them in from the app. They live in the
   AppData folder, so image updates keep them.

Notes:

- `OMB_LAN=1` makes the server listen beyond the container. It still refuses connections from
  public addresses: only private ranges (10/8, 172.16/12, 192.168/16, Tailscale 100.64/10 and
  link-local) get through, and each device must pair.
- The container runs as `99:100` (nobody:users), so Unraid-created appdata folders work as is.
- Plain HTTP is unencrypted. For access beyond your LAN, use Tailscale Serve or an HTTPS reverse
  proxy and set Public URL to that address.
- **Webhooks** (`/hooks/*`, for GitHub, Stripe and other services) use their own receiver, which
  only listens inside the container. To reach it from the internet, give it a Unix socket and point
  a proxy at that socket:
  1. Set the advanced **Webhook socket folder** to a host folder outside AppData (bots can read
     AppData), for example `/mnt/user/appdata/openmausbot-run`, and set **Webhook socket** to
     `/run/openmausbot/hooks.sock`.
  2. Mount the same folder into your proxy. With Cloudflare Tunnel, mount it into the cloudflared
     container (for example at `/omb`) and add a public hostname with path `^/hooks/`, service type
     **UNIX** and URL `/omb/hooks.sock`. The tunnel then exposes only the webhook paths.
  3. Set **Webhook public URL** to that hostname (`https://hooks.example.com`) so new hook URLs
     use it. Each hook URL carries its own secret `wh_…` token. The app itself stays private.

## error-pages

[error-pages](https://github.com/tarampampam/error-pages) (MIT, by tarampampam) serves themed HTTP
error pages (404, 502, 503 and others) for a reverse proxy. The template runs the upstream image
`tarampampam/error-pages:4` as published.

- For Traefik, put the container on Traefik's Docker network and add an `errors` middleware with
  `service: http://error-pages:8080` and `query: /{status}.html`. Middlewares apply only to routes
  that match, so an unknown hostname still gets Traefik's own plain 404.
- The host port is only needed to preview the pages or for a proxy on another network. Unraid's web
  UI may already use 8080, so pick another port if so.
- Error pages are served as HTML, JSON, XML or plain text, depending on the request's `Accept` header.

## Nod

[Nod](https://nod.n8n.io) is a self-hosted personal AI assistant from the n8n team. Upstream
ships it as a [Docker Compose stack](https://nod.n8n.io/docs/deploy/self-host/). These templates
run the same six containers as separate Unraid apps.

> Unofficial community packaging, not affiliated with or endorsed by n8n GmbH.
> Nod is © n8n GmbH, licensed under Apache-2.0. See its [NOTICE](https://github.com/n8n-io/nod/blob/main/NOTICE)
> for bundled components, including a GPL-3.0-or-later speech component whose source is in the upstream repository.

| # | Template | Image | Network | Runs as | Role |
|---|---|---|---|---|---|
| 1 | `nod-postgres` | `ghcr.io/repires/nod-postgres` | `nod` | postgres | PostgreSQL 17 (official `postgres:17-alpine` with a healthcheck) |
| 2 | `nod-runtime` | `ghcr.io/repires/nod-runtime` | `nod` | root, with the Docker socket | Filtered Docker API: only lets `nod-server` exec into the workspace and browser |
| 3 | `nod-browser-unraid` | `ghcr.io/repires/nod-browser` | `bridge` | uid 1000 | Headless browser |
| 4 | `nod-workspace-network` | `ghcr.io/repires/nod-workspace` | `bridge` | root, `NET_ADMIN` | Firewall for the workspace: public internet only |
| 5 | `nod-workspace-unraid` | `ghcr.io/repires/nod-workspace` | `container:nod-workspace-network` | uid 1000 | Command and file sandbox |
| 6 | `nod-server` | `ghcr.io/repires/nod-server` | `nod`, port 4310 | uid 1000 | App and API |

### Install

1. Create the shared network once, in the Unraid terminal: `docker network create nod`.
   Templates 1, 2 and 6 attach to it. If it is missing, Unraid starts them with no network.
2. Pick a database password made of letters and digits, for example from `openssl rand -hex 24`.
3. Install the templates **in the order above**. Enter the same database password in
   `nod-postgres` and `nod-server`.
4. Nod requires **HTTPS**. Point a reverse proxy (SWAG, Nginx Proxy Manager, Traefik) or
   Tailscale Serve at port 4310, and set `nod-server`'s **Public URL** to that exact origin, for
   example `https://nod.example.com`. Nod only answers requests for that origin, so opening
   `http://<server>:4310` directly returns 403. That is also why the template has no WebUI link.
5. On first start `nod-server` generates `NOD_AUTH_TOKEN` and `NOD_VAULT_KEY` in
   `/mnt/user/appdata/nod/server/secrets.env` (unless you set them in the template's Advanced
   view). Sign in with `NOD_AUTH_TOKEN`, then connect a model under **Models**.
   **Back up `NOD_VAULT_KEY`:** without it, saved credentials cannot be decrypted.

### Notes

- **Container names:** keep them. `nod-server` and `nod-runtime` find the workspace and browser
  by name, and the runtime only accepts names starting with `nod-workspace-` and `nod-browser-`.
- **Restart order:** after restarting or updating `nod-workspace-network`, restart
  `nod-workspace-unraid`. Compose does this automatically; Unraid does not.
- **Hardening:**
  - The server, browser, runtime and workspace firewall have a read-only root filesystem.
  - The server, browser and workspace drop all capabilities except `CHOWN`, `SETUID` and
    `SETGID`. Their entrypoint uses these as root to give new appdata folders to uid 1000,
    then runs Nod as the `node` user. The runtime drops all capabilities, and the firewall
    keeps only `NET_ADMIN`.
  - Those five containers also set `no-new-privileges` and memory and process limits.
    `nod-postgres` runs with the official Postgres image's defaults.
- **Isolation compared with upstream's Compose stack:**
  - Kept: the workspace firewall blocks LAN, Tailscale (`100.64.0.0/10`), Docker and other
    private ranges, and the runtime only allows exec into the two Nod containers.
  - Relaxed: upstream also puts the database and runtime on internal networks with no internet
    access, and the browser on its own network. Here they share the user-created `nod` bridge,
    and the browser uses Unraid's default bridge.
- **Telemetry:** analytics and in-app feedback to the Nod team are off by default.

### Images

[`.github/workflows/nod-images.yml`](.github/workflows/nod-images.yml) publishes five images to
`ghcr.io/repires`. It runs daily, on manual dispatch, and on pushes that change `images/nod`.
The daily run does nothing if the latest upstream release is already published.

1. **`nod-server`, `nod-browser`, `nod-workspace`:** built from the upstream release tag with
   upstream's own Dockerfiles, plus the wrappers in [`images/nod`](images/nod). The wrappers add
   the appdata-ownership entrypoint, secret generation and healthchecks.
2. **`nod-runtime`:** `node` with the release's `docker-proxy.mjs`.
3. **`nod-postgres`:** `postgres:17-alpine` with Nod's database defaults and a healthcheck.

Each image is tagged `:<version>` and `:latest`, and the templates use `:latest`, so Unraid
shows an update when a new Nod release is published. To rebuild a specific release, run the
workflow manually with its tag (`nod-vX.Y.Z`) and **force** enabled.

## Support

Report template or image problems in this repository's
[issues](https://github.com/repires/unraid-templates/issues). Report problems in the apps
themselves upstream: [ai-memory](https://github.com/akitaonrails/ai-memory/issues),
[OpenMausBot](https://github.com/milind-soni/OpenMausBot/issues),
[error-pages](https://github.com/tarampampam/error-pages/issues), [Nod](https://github.com/n8n-io/nod/issues).

## License

The templates, wrappers and workflow in this repository are MIT licensed. ai-memory is MIT
(Fabio Akita), OpenMausBot is Apache-2.0 (Milind Soni), error-pages is MIT (tarampampam) and Nod is
Apache-2.0 (n8n GmbH).
