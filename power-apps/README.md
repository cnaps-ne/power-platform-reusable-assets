# Canvas Power Apps assets

## Two asset classes

- `references/third-party/pnp-powerplatform-snippets/` contains unmodified MIT-licensed community snippets with their original README and licence.
- `power-apps/` contains generic copy/paste patterns and native Canvas component source created for this library.

The local files ending `.controls.yaml` are **paste-code control fragments**, not complete unpacked app files. Paste them into a screen or component tree in Power Apps Studio. Control versions follow working public PnP snippets and should still be checked against the target app's serialized source.

The native component collection is indexed in
`power-apps/components/canvas-native/README.md`. It contains 20 components,
including application/portal headers, navigation, loading, activity, stepper,
cards, pills and empty states.

## Expected data

`colNavigation`, `colWorkQueue`, `colRequestTypes`, `varSelectedWorkItem`, `varShowLoading` and `varShowPanel` are deliberately generic integration points. Rename them to match the consuming app.

## Import risks

- Power Apps YAML is version-sensitive. A control version may be rewritten by Studio.
- Paste-code can require cutting and repasting a formula after control names resolve.
- SharePoint delegation must be rechecked with real list sizes and indexed fields.
- Imported snippets do not create data sources, collections, screens, component properties or security.
- Full `ComponentDefinitions:` files are review/copy sources and are not a substitute for a complete app package.
- Creator Kit references are intentionally not embedded; using them adds a managed solution/PCF dependency.
