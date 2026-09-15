# Recommended first-release subset

The fastest credible first release uses native responsive containers, SharePoint-backed galleries and only one imported component.

## Use now

1. `power-apps/layouts/application-shell.controls.yaml` — one shell for portal and operator screens; change the navigation collection by role.
2. `power-apps/forms/request-form-layout.controls.yaml` — request submission frame.
3. `power-apps/galleries/filter-bar.controls.yaml` plus `work-queue-gallery.controls.yaml` — IT operational workspace.
4. `power-apps/components/kpi-strip.controls.yaml` — four useful queue counts without a separate dashboard build.
5. PnP `confirmation-dialog` — reusable confirmation for assign, close, reject and CAB actions.
6. PnP `activity-feed` — comments/status history on detail screens.
7. SharePoint `status-pill.json`, `priority-badge.json`, `due-date-indicator.json`, `person-chip.json` and `assign-to-me.json`.
8. `sharepoint/work-queue/operational-view.json`, `my-requests-view.json` and `delivery-pipeline/delivery-pipeline-view.json`.

## Use only if time remains

- `responsive-hero-cards-gallery` for a richer request catalogue.
- `notification-toaster` if native `Notify()` is visibly insufficient.
- Work Queue card view for lower-volume triage.
- Progress-step component when the submission or delivery process genuinely has multiple user-visible stages.

## Defer

- Creator Kit/PCF controls unless already approved and deployed.
- Drag-and-drop Kanban.
- Custom pagination; start with delegated SharePoint queries and indexed columns.
- Dashboard-only screens; embed the four operational KPIs in the workspace.
- Timeline-style SharePoint views for CAB; a filtered/grouped compact delivery view is faster and easier to operate.

## Suggested build order

1. Agree list columns, choice values, indexes and permissions.
2. Build shell and role-specific navigation.
3. Build request submission and confirmation.
4. Build My Requests and deep link to detail.
5. Build operator queue, assign-to-me and detail/activity panel.
6. Build Delivery Pipeline and filtered CAB view.
7. Add polish only after the end-to-end paths work.
