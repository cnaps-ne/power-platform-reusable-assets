# Canvas pattern matrix

| Need | Selected asset | Decision |
|---|---|---|
| Application shell | Local responsive shell | Use in Rev 1 |
| Header/navigation | Shell plus `colNavigation` | Use; one generic structure with role-filtered items |
| Search/filter bar | Local filter bar | Use in operator workspace |
| Dense work queue | Local gallery | Use in operator workspace |
| Request cards/categories | PnP responsive hero cards | Optional polish |
| KPI cards | Local KPI strip | Use; avoid a separate dashboard initially |
| Empty/loading states | Local fragments | Use where asynchronous loading is visible |
| Confirmation dialog | PnP confirmation dialog | Use once across app |
| Side panel | Local side panel | Optional quick detail pattern |
| Detail timeline/comments | PnP activity feed | Use after mapping its generic fields |
| Request submission | Local request form frame | Use, then connect real Patch/SubmitForm logic |
| Multi-step form | PnP progress-step | Defer unless the request form genuinely needs steps |
| Breadcrumbs | PnP breadcrumbs | Defer for initial shallow navigation |
| Toasts | PnP notification toaster | Defer; native `Notify()` is faster |
| Pagination | Local Power Fx reference | Defer; prefer delegated filters and indexed columns |
| Advanced table/command bar/tabs | Creator Kit | Reference only; dependency cost is too high for the initial week |
