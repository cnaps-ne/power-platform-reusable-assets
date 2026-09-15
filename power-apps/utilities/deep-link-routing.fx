// App.StartScreen example. Rename screens and parameter to match the consuming app.
If(
    !IsBlank(Param("itemId")) && IsNumeric(Param("itemId")),
    'Work Item Detail Screen',
    'Home Screen'
)
