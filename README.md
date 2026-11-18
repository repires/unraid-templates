# Unraid templates by repires

Community Applications templates for Unraid.

## Nod

[Nod](https://nod.n8n.io) is a self-hosted personal AI assistant from the n8n team.
Upstream ships it as a Docker Compose stack. These templates install the same six
containers through the Unraid Docker tab, with the same isolation.

> Unofficial community packaging, not affiliated with or endorsed by n8n GmbH.
> Nod is © n8n GmbH, licensed under Apache-2.0. See its [NOTICE](https://github.com/n8n-io/nod/blob/main/NOTICE)
> for bundled components, including a GPL-3.0-or-later speech component whose source is in the upstream repository.

| # | Template | Image | Network | Role |
|---|---|---|---|---|
| 1 | `nod-postgres` | `ghcr.io/repires/nod-postgres` | `nod` | PostgreSQL 17 |
| 2 | `nod-runtime` | `ghcr.io/repires/nod-runtime` | `nod` | Filtered Docker API: exec into the workspace and browser only |
| 3 | `nod-browser-unraid` | `ghcr.io/repires/nod-browser` | `bridge` | Headless browser |
| 4 | `nod-workspace-network` | `ghcr.io/repires/nod-workspace` | `bridge` | Firewall: public internet only, LAN/Tailscale/private ranges blocked |
| 5 | `nod-workspace-unraid` | `ghcr.io/repires/nod-workspace` | `container:nod-workspace-network` | Command and file sandbox |
| 6 | `nod-server` | `ghcr.io/repires/nod-server` | `nod`, port 4310 | App and API |

### Install

1. Create the shared network once, in the Unraid terminal: `docker network create nod`
2. Pick a database password made of letters and digits, for example from `openssl rand -hex 24`.
3. Install the templates **in the order above**. Enter the database password in `nod-postgres` and `nod-server`.
4. Nod requires **HTTPS**. Point a reverse proxy (SWAG, Nginx Proxy Manager, Traefik) or Tailscale Serve at port 4310. Then set `nod-server`'s **Public URL** to that exact address, for example `https://nod.example.com`. Opening `http://<server>:4310` directly returns 403.
5. Sign in with `NOD_AUTH_TOKEN` from `/mnt/user/appdata/nod/server/secrets.env`, which is generated on first start. **Back up `NOD_VAULT_KEY`** from the same file. Then connect a model under **Models**.

### Notes

- Keep the container names. `nod-server` and `nod-runtime` find the workspace and browser by name (`nod-workspace-*` and `nod-browser-*`).
- After restarting or updating `nod-workspace-network`, restart `nod-workspace-unraid`.
- Containers run as uid 1000 with a read-only root filesystem and all capabilities dropped. On start they briefly keep `CHOWN`/`SETUID`/`SETGID` to give new appdata folders to uid 1000, then drop to the `node` user.
- Analytics and in-app feedback to the Nod team are off by default.

### Images

`.github/workflows/nod-images.yml` checks for a new upstream release daily. For each one it:

1. builds the three upstream images exactly as `deployment/self-host/compose.yaml` does;
2. adds the small wrappers in `images/nod`;
3. pushes `:<version>` and `:latest` to GHCR.

To rebuild a specific release, run the workflow manually with its tag.

## License

The templates, wrappers and workflow in this repository are MIT licensed. Nod itself is Apache-2.0 (n8n GmbH).
