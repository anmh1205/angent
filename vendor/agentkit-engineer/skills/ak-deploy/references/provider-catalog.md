# Deployment provider catalog

Use this as recognition/routing knowledge, not as a frozen command or pricing table.

| Signal / family | Likely provider |
|---|---|
| `vercel.json`, `.vercel/` | Vercel |
| `netlify.toml`, `_redirects` | Netlify |
| `wrangler.toml/json` | Cloudflare |
| `fly.toml` | Fly.io |
| `railway.json/toml` | Railway |
| `render.yaml` | Render |
| `Procfile` / provider app metadata | Heroku-compatible / inspect project docs |
| `tose.yaml/json` | TOSE |
| Coolify metadata + Docker/Compose | Coolify |
| `dokploy.yml` or project docs | Dokploy |
| GitHub Pages workflow/config | GitHub Pages |
| GCP app/Cloud Run config | Google Cloud |
| AWS Amplify/build/deployment config | AWS |
| `.do/app.yaml` | DigitalOcean |
| explicit Vultr config/docs | Vultr |

Signals are hints. Existing project docs/provider IDs/current account state outrank heuristic detection.

## Project-type recommendation

When the project has no established provider, derive candidates from requirements:
- static site;
- SPA;
- SSR/full-stack;
- API/service;
- Docker workload;
- monorepo;
- self-hosted/enterprise constraints.

Compare current cost/limits, runtime compatibility, regions, persistence, networking, secrets, preview/prod workflow and operational constraints using current official sources. Do not repeat historical "free tier" figures from the pinned package as current fact.

## Provider execution

For the selected provider:
1. inspect project config;
2. inspect installed CLI/API/connector capability;
3. inspect current provider help/docs when syntax/effects matter;
4. authenticate without exposing credentials;
5. deploy the resolved artifact;
6. read back exact provider state;
7. verify the user-facing endpoint.

Load only the provider information needed for the selected target.
