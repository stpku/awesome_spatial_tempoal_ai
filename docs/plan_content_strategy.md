# Content Strategy Plan — Depth, Richness, Update Pace

Owner: Awesome Spatio-Temporal AI
First published: 2026-01-21
Next review: 2026-02-01

## 1. Objectives

- Depth: provide expert-grade context and synthesis per entry (why it matters, how it works, limitations, reproducibility).
- Richness: broaden coverage across domains, modalities, data types, and stakeholders (academia, industry, OSS, datasets, benchmarks, media).
- Update pace: sustain predictable weekly refreshes and monthly summaries with measurable SLAs.

### KPIs (tracked monthly)
- Depth score ≥ 0.8 (editorial checklist pass rate). Target: ≥ 90% of new entries.
- Coverage growth: +8–15 vetted entries/week, ≥ 1 new sub-domain per month.
- Freshness: stars refreshed weekly; broken-link rate ≤ 2%; median time-to-publish ≤ 7 days.

## 2. Metadata Model (per category)

All JSON entries must include the following enriched fields (beyond name/url/description):

### Projects (OSS/Research)
- fields: name, url, description, tech_stack[], stars, last_updated, license, maturity (research/prod), modality (image/video/3D/geo), domain (robotics/remote-sensing/traffic/weather/etc.), spatial_scale (object/scene/city/earth), temporal_scale (ms/sec/min/day/month), key_methods (e.g., world model, diffusion, transformer), datasets_used[], benchmarks[], limitations, reproducibility (paper/code/data availability).

### Papers
- fields: title, url, year, venue, authors, domain, modality, method, datasets_used[], metrics (SOTA? baseline comparison), limitations, reproducibility (code/data links), impact_summary (2–4 bullets), tags[].

### Datasets
- fields: name, url, description, license, provider, domain, modality (raster/vector/point), spatial_resolution, temporal_resolution, coverage (geo-region/period), tasks_supported (classification/detection/forecasting), access (API/download), citation.

### Conferences/Journals
- fields: short_name, full_name, url, scope (domains), categories[], submission_deadline (if applicable), typical topics, relevance_to_ST_AI.

### Media (WeChat/Newsletters)
- fields: name, url (if available), language, focus_areas, cadence, notable_series.

## 3. Editorial Workflow

### Intake sources (continuous)
- arXiv RSS: cs.CV, cs.LG, stat.ML, robotics; earth science (for remote sensing/time series).
- Proceedings: CVPR/ICCV/ECCV/NeurIPS/ICML/ICLR/RSS/SIGSPATIAL.
- GitHub trending/awesome lists with queries: "spatiotemporal", "world model", "geospatial", "remote sensing".
- OSGeo ecosystem (GRASS, GDAL, QGIS, PostGIS), Open Data Cube, TorchGeo.
- Chinese media: UrbanComp、GeoAI前沿、燕园时空、未名时空等。

### Triage (48h SLA)
- Duplicate detection: same url/name across files.
- Quick fit: relevant to spatial-temporal AI or world models; reject if tangential.
- Minimum metadata completeness: name/url/description + 5 core enriched fields.

### Deep review (≤ 7 days)
- Two-editor sign-off using checklist: 
  - Why it matters (2–3 bullets), How it works (method/architecture), Limitations, Reproducibility.
  - Links validated (HTTP 200/3xx); license present; tags consistent.
- Depth-quality gate: entries missing limitations or reproducibility notes are flagged.

### Publish & summarize
- Update JSON + regenerate summaries (README sections, monthly report).
- Sort entries (projects by stars+recency; papers by year+venue).
- Add "impact_summary" for high-value items.

## 4. Automation Backlog (to support pace)

- JSON Schema enforcement per file (schemas/*.json) in CI.
- Weekly stars refresh via GitHub REST API with batching, rate limit handling, auto PR.
- Monthly broken-link scan (HEAD/GET with timeouts), auto report in reports/ and auto Issue.
- Stale detection (last_updated > 90 days) → flag and prioritize refresh.
- Pre-commit hooks: json formatting, trailing whitespace, EOF fixer, ruff+black for scripts.

## 5. Coverage Expansion Map (next 3 months)

- World models: Genie2, DreamerV3, PlaNet successors, robotic world models (SpatialVLA, Marble), simulation platforms.
- Spatiotemporal forecasting: weather/climate (ERA5, ClimSim), traffic/mobility (METR-LA, PeMS), remote sensing time series (Sentinel/Landsat).
- Geospatial ML foundations: vector/raster ops (GeoPandas, PySAL, TorchGeo), data cubes (Open Data Cube, rasdaman), spatial DBs (PostGIS, MobilityDB).
- Benchmarks: curated list of datasets+tasks+metrics; call out evaluation gaps.
- Industry & APIs: geospatial providers, managed platforms, ST APIs (mapping/weather/POI).

## 6. Cadence & KPIs

### Weekly (every Monday)
- Stars refresh and merge PR.
- Add 8–15 new entries (mix across domains), fix broken links.
- Median time-to-publish ≤ 7 days.

### Monthly (1st of month)
- Publish summary report (changes, trends, broken-link stats, stale entries count).
- At least 2 deep dives (long-form notes added to high-impact projects/papers).
- Coverage metric review: ensure ≥ 1 new sub-domain.

### Metrics collection
- CI generates reports/summary.json + reports/summary.md with counts, failures, stale items.
- README badges: last update date, total entries, broken-link rate, stale count.

## 7. Governance & Tracking

- GitHub Projects board: Intake → Triage → Deep review → Ready → Published.
- Labels: new-project, dataset, paper, conference, journal, media, deep-dive, stale, broken-link.
- Maintainers roster with weekly rotation; triage SLA 48h; review SLA 7 days.
- This plan file tracks revisions (see history) and upcoming milestones.

## 8. Implementation Phasing

Phase 1 (Weeks 1–2)
- Define JSON Schemas; add CI schema validation.
- Add weekly stars workflow + auto PR.
- Link-check script with monthly report generation.
- Update contribution guide with enriched fields + PR checklist.
- Add README badges and counts.

Phase 2 (Weeks 3–6)
- Depth-quality editorial checklist; require limitations + reproducibility.
- Stale detection + prioritization.
- Pre-commit hooks; ruff+black for scripts.
- Sorting rules and auto formatting of JSON.

Phase 3 (Weeks 7–12)
- Monthly summaries auto-generated; deep-dive notes for top items.
- Coverage expansion across planned sub-domains.
- Optional docs site (MkDocs + i18n) generated from JSON.

## 9. Risks & Mitigations

- API rate limits → batch requests + caching + backoff.
- Link volatility → retries + whitelist + classify soft failures as warnings.
- Editor bandwidth → rota + smaller weekly targets if needed.

## 10. Revision History

- 2026-01-21: Initial version aligned to depth, richness, update pace objectives.
