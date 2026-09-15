# Research summary

## Findings

- PnP List Formatting is the highest-value source for SharePoint status, person, row-action, flow, card and timeline patterns. Its MIT licence permits copying and adaptation when the notice is retained.
- PnP Power Platform Snippets is the strongest source found for paste-ready Canvas YAML. The confirmation dialog and activity feed directly reduce first-release build effort.
- Creator Kit is the broadest professional component set, but its managed-solution and PCF footprint is a delivery dependency rather than a free paste-code shortcut.
- Native Microsoft Lists board views can be useful, but JSON tile formatting is presentation rather than a full workflow engine or secure data filter.

## Technical cautions

- JSON formatting is UI only. It cannot replace permissions, validation, automation, list indexes or view filters.
- `executeFlow` samples require a real flow ID and permissions in the target tenant.
- Power App deep links require the target app web link plus matching `Param()` routing.
- `setValue` actions depend on exact internal field names and the user's edit permission.
- Power Apps YAML is version-sensitive and should be pasted/tested in a development copy before wider reuse.
