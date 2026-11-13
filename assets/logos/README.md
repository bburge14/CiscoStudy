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

## Optional: per-cert badges

To give a single track its own badge (instead of the issuing-body logo),
drop a file in the `certs/` subfolder named by the track's exam key:

```
assets/logos/certs/ccna.svg      assets/logos/certs/cissp.svg
assets/logos/certs/secplus.svg   assets/logos/certs/clf.svg   ...
```

When present, the badge shows at the right of that track's page header and
takes precedence over the provider logo. Entirely optional — provider logos
alone look great.

## Note

These are third-party trademarks, included here only for a personal, local
study tool. Any file you add stays in your own repo.
