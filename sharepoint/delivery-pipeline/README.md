# Delivery Pipeline

`delivery-pipeline-view.json` is a compact projects-and-changes view. It expects `DeliveryRef`, `Title`, `DeliveryType`, `Owner`, `Status`, `ApprovalStatus`, `RiskRating` and `TargetDate` in the view.

For CAB, create a separate filtered SharePoint view such as `ApprovalStatus = Pending` and group by the meeting/date field. Keep approval actions in Power Apps or Power Automate unless list-level action buttons are explicitly required.
