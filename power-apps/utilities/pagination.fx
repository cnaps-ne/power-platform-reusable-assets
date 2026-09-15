// Gallery.Items example for local collections. pageSize and pageNumber are numeric variables.
FirstN(
    LastN(
        SortByColumns(colWorkQueue, "Created", SortOrder.Descending),
        Max(0, CountRows(colWorkQueue) - ((pageNumber - 1) * pageSize))
    ),
    pageSize
)
