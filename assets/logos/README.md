# Provider logos (drop-in)

Put each issuing body's logo here and it appears automatically in the track
picker (sidebar -> **Active track**), grouped by issuing agency. No code
changes needed - the app reads these files at startup.

## Filenames

SVG is preferred; PNG or WebP also work (first match wins per provider):

| File | Provider |
|------|----------|
| `cisco.svg` | Cisco |
| `comptia.svg` | CompTIA |
| `isc2.svg` | (ISC)² |
| `isaca.svg` | ISACA |
| `ec-council.svg` | EC-Council |
| `aws.svg` | AWS |
| `microsoft.svg` | Microsoft |

## Tips

- **The sidebar is dark** - use a white/light or full-color logo, not black
  ink, or it won't be visible. (Many vendors publish a "reverse"/"white"
  variant for dark backgrounds.)
- An **icon/symbol** mark reads better than a full wordmark - the provider
  name is shown beside it.
- Rendered ~16px tall, width auto (capped ~96px). Use a transparent
  background.
- Until a file is present for a provider, the picker just shows the provider
  name - nothing breaks.

## Note

These are third-party trademarks, included here only for a personal, local
study tool. Any file you add stays in your own repo.
