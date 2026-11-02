# SchemePulse government-scheme sync

This is a **public, automation-only** repository for a scheduled, source-specific government-scheme catalogue poller. It is separate from the SchemePulse application repository. Never commit API keys, bearer tokens, webhook tokens, or private data here; store credentials only as GitHub Actions Secrets.

## Current status

The repository is a guarded starter, **not a live integration yet**. No official API sources or SchemePulse ingest endpoint are configured, and the workflow is disabled unless the repository variable `SCHEME_SYNC_ENABLED` is set to `true`. Do not enable it until an official API, its access conditions, a source adapter, and the receiving SchemePulse endpoint have been verified and implemented. Do not scrape undocumented portal endpoints.

## Why GitHub Actions

GitHub-hosted standard runners remain free for public repositories. A scheduled workflow is serverless, so it does not need a continuously running computer. GitHub describes scheduled executions as best-effort: they may be delayed or, during high load, dropped. Public-repository scheduled workflows are disabled after 60 days without repository activity. This is periodic polling, not a guarantee of instant updates. See [GitHub Actions billing](https://docs.github.com/billing/managing-billing-for-github-actions/about-billing-for-github-actions) and [schedule events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

## Source onboarding requirements

For each source, confirm that it publishes an official, documented API that includes scheme records; determine whether access requires registration, approval, or a key; read its rate limits and terms; and establish how pagination and full snapshots work. API Setu is a discovery/access platform, so availability and authorization must be checked per API. The public MyScheme site reviewed so far does not publish a developer catalogue API specification; no endpoint is assumed. Start with `sources.example.json` only after the source is verified.

## Change and removal policy

Use stable identifiers scoped by source. Add a record when an ID first appears; treat a changed normalized payload or source update timestamp as an update. Never hard-delete a scheme merely because a request failed or a partial page omitted it. A future adapter may mark a record inactive only after a complete, successful, paginated snapshot confirms it is missing, with a source-specific safety threshold and audit record. Preserve the last known record and its official source link for review.

## Integration contract to implement

A source adapter must fetch only documented read-only endpoints, normalize a complete source record, retain the upstream identifier and source timestamp, and send idempotent changes to a protected SchemePulse ingest endpoint. The receiving application must validate the payload, authenticate the sender, record sync freshness and source provenance, and update the public catalogue without exposing credentials. Until that endpoint and adapters exist, this repository makes no government API calls and delivers no catalogue updates.

## Local checks

The starter's preflight guard is intentionally fail-closed if the workflow is enabled before a source registry exists. Keep `SCHEME_SYNC_ENABLED` unset until the actual source adapters and receiver are ready.
