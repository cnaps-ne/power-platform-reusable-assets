# Native Canvas component library

This folder contains 20 generic Canvas components for request, incident, work-queue and delivery-management apps.

- `source/` contains complete `ComponentDefinitions:` source files.
- `paste/` contains control-only paste-code for the 14 design-option components.
- The six **exported** components came from a functioning Canvas app export.
- The fourteen **draft** components follow the same observed control versions and property structure, but still require Studio compilation and testing.

The components contain no tenant URLs, credentials, organisation branding or implementation-specific data sources. They use generic named-formula integration points rather than embedding a SharePoint schema.

## Component catalogue

| Component | Status | Purpose | Paste YAML |
|---|---|---|---|
| `cmpActivityTimeline` | Exported | Filterable activity/audit timeline with loading state and expandable entries | No |
| `cmpHeader` | Exported | Compact workspace header with theme toggle and user identity | No |
| `cmpLoadingScreen` | Exported | Branded loading experience with progress steps and error state | No |
| `cmpNav` | Exported | Full-height application navigation | No |
| `cmpPortalHeader` | Exported | Full-width requester portal header with tabs and notifications | No |
| `cmpStepper` | Exported | Step and bar progress indicator | No |
| `cmpActivityItem` | Draft | Compact individual activity entry | Yes |
| `cmpCategoryCard` | Draft | Service/request category card | Yes |
| `cmpEmptyState` | Draft | Empty, no-results or unavailable state | Yes |
| `cmpHeaderClean` | Draft | Calm workspace header option | Yes |
| `cmpHeaderCommand` | Draft | Command-oriented workspace header option | Yes |
| `cmpHeaderGlow` | Draft | Accent-glow workspace header option | Yes |
| `cmpMetricCard` | Draft | KPI/metric card with reporting scope | Yes |
| `cmpPortalHeaderMinimal` | Draft | Minimal requester portal header option | Yes |
| `cmpPortalHero` | Draft | Search-led portal hero with accent glow | Yes |
| `cmpPriorityPill` | Draft | Priority badge driven by a priority palette | Yes |
| `cmpRequestCard` | Draft | Read-only request/work-item summary card | Yes |
| `cmpRoleNav` | Draft | Role-rank-aware navigation alternative | Yes |
| `cmpSectionHeader` | Draft | Consistent section title and description | Yes |
| `cmpStatusPill` | Draft | Status badge with optional requester-facing progress | Yes |

## Expected app-scope integration

The components intentionally use the following generic app-level names. Either create compatible named formulas or replace the references after import:

- Theme: `nfThemePrimary`, `nfThemeSecondary`, `nfThemeBackground`, `nfThemeSurface`, `nfThemeText`, `nfThemeMutedText`, `nfThemeBorder`, `nfThemeHover` and text-colour equivalents.
- Layout: `nfHeaderHeight`, `nfNavWidth`, `nfPagePadding`, `nfButtonHeight`, `nfInputHeight`, `nfCardRadius` and `nfControlRadius`.
- Typography: `nfAppFont` and the `nfFontSize*` formulas.
- Navigation: `nfNavMenu` with `Title`, `Screen`, `Icon`, `MinRoleRank`, `SortOrder`, `Group` and `IsSection`.
- User/theme state: `gblDarkMode`, `gblIsAdmin`, `nfCurrentUserEmail` and `nfCurrentUserRoleRank` where referenced.
- Visual helpers: `fnIconHtml`, `fnSurfaceGradient`, `nfIconLibrary` and `nfThemeLogo`.
- Request metadata: `nfStatuses`, `nfProgress`, `nfPriorities` and `nfActivityTypes`.

## Import approach

1. Create a blank component with the same name in Power Apps Studio.
2. Enable **Access app scope** when the component uses app-level named formulas.
3. Recreate the custom properties shown near the top of the matching source file.
4. For components with a paste file, paste the `paste/*.controls.yaml` content into the component tree.
5. Bind event properties such as `OnOpen`, `OnReady` or `OnNotificationSelect` on the component instance.
6. Test in a copied screen before replacing an existing application component.

## Known risks

- Canvas YAML and control versions are preview/version-sensitive; Studio may rewrite them.
- Full `.pa.yaml` files are source references, not standalone import packages.
- Paste-code does not create custom properties, named formulas, data sources or screens.
- Some navigation/header examples include generic screen names such as `Queue Screen`; replace those destinations in the consuming app.
- The exported components are proven in their source app, but the sanitised public copies have not been round-tripped through a new `.msapp`.
- The draft components have not yet been compiled in Studio.
