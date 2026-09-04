# Vendored React 18.2.0 UMD builds

Used only by `pipeline/publish.py --standalone`, which produces the emailable
single-file dashboard. That file has to open by double-click on a machine with
no network guarantee, so React is inlined rather than pulled from a CDN.

The published Artifact keeps the pinned cdnjs URLs instead: cdnjs is on the
Artifact CSP allowlist, and leaving it external keeps the page smaller.

Source: `npm pack react@18.2.0 react-dom@18.2.0`, `umd/*.production.min.js`.
Pinned deliberately; if you bump the version, bump the CDN URLs in publish.py
to match so the two builds stay on the same React.
