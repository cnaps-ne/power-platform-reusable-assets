# SharePoint formatting

All local formats use generic internal names. Confirm the internal names in the target list before applying JSON; display names are not sufficient.

## Work Queue fields

| Internal name | Type | Notes |
|---|---|---|
| `RequestRef` | Single line text | Human-readable reference |
| `Title` | Single line text | Summary |
| `RequestType` | Choice/text | Request, incident or work type |
| `Status` | Choice | New, Assigned, In Progress, Waiting, Resolved, Closed, Cancelled |
| `Priority` | Choice | Critical, High, Normal, Low |
| `SubmittedBy` | Person | Single person |
| `AssignedTo` | Person | Single person |
| `AssignedTeam` | Choice/text | Generic team label |
| `Created` | Date/time | Built-in column |
| `DueDate` | Date/time | Optional |
| `SLAStatus` | Choice | Breached, At Risk, On Track, Paused, Met |
| `IsOverdue` | Yes/No | Prefer deterministic automation/calculation |

## Delivery Pipeline additions

`DeliveryRef`, `DeliveryType`, `Owner`, `TargetDate`, `ApprovalStatus`, `RiskRating`, `Progress` and `NextMilestone`.

Apply column formats from **Column settings → Format this column → Advanced mode**. Apply view formats from **Format current view → Advanced mode**. View formatting does not filter records or grant security; create the documented SharePoint view filters separately.
