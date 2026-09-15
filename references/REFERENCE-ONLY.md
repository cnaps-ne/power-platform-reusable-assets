# Reference-only catalogue

These sources were reviewed but not copied into the reusable library.

## Microsoft Creator Kit

https://github.com/microsoft/powercat-creator-kit — MIT.

Useful controls include DetailsList, Command Bar, Dialog, Panel, Pivot/Tabs, Breadcrumb and Pagination. It can greatly improve complex operator UIs, but it adds a managed-solution/PCF dependency and environment setup. Reconsider after the first release or use it only if already approved and installed.

## Power CAT code components

https://github.com/microsoft/powercat-code-components — MIT.

The lower-level PCF source behind many Fluent components. Reference only because copying individual source folders would not produce a paste-ready Canvas asset and would create a build/deployment burden.

## Microsoft Power Apps Samples

https://github.com/microsoft/PowerApps-Samples — MIT.

Strong for platform APIs, PCF and wider samples, but it did not provide a sufficiently focused set of paste-ready queue/CAB Canvas YAML assets for this library.

## Microsoft Power Platform Skills

https://github.com/microsoft/power-platform-skills — MIT.

Useful current guidance for `.pa.yaml`, responsive layout and QA. It is tooling/documentation rather than a user-facing component library, so it remains a reference.

## Samples deliberately not copied

- Full helpdesk or ticketing applications: too much inherited schema, environment configuration and business logic.
- Large all-in-one pop-in snippet: over 200 KB, several behaviours coupled together, and slower to understand than using one confirmation dialog plus one loading overlay.
- Decorative animation/game/chart snippets: no meaningful Rev 1 delivery benefit.
- Drag-and-drop galleries and pseudo-Kanban interactions: fragile, more testing, and no requirement for drag/drop in Rev 1.
- Unlicensed gists, blog-only code and repositories without a clear licence: redistribution rights are unclear.
- Tenant-branded templates and screenshots: not generic and may leak implementation details.
