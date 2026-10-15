# llms.txt format and destination contract

Pinned Engineer 2.19.0 uses the [llmstxt.org](https://llmstxt.org/) proposal:

- One H1 project/site name (**mandatory**).
- Concise blockquote overview (**recommended**).
- Optional explanatory prose.
- H2 sections grouping canonical documentation links.
- Link entries `- [Title](https://example.com/docs/page): Brief description`.
- A final `## Optional` section for links readers/LLMs can omit in shorter context windows.

Example:

~~~markdown
# Project Documentation

> Official documentation for setup, APIs and operating the project.

## Getting Started

- [Install](https://docs.example.com/install): Environment setup and first run
- [Quickstart](https://docs.example.com/quickstart): Minimal working example

## API Reference

- [API](https://docs.example.com/api): Public routes and authentication

## Optional

- [History](https://docs.example.com/history): Older release notes
~~~

The default `llms.txt` is a curated linked index. Optional `llms-full.txt` inlines selected source content and must not silently include a larger confidentiality scope than the index. Neither file changes the official documentation authority. Validate live URLs only where actual network access and permission exist; otherwise report unverified link reachability.
