# SchemaFirst UTM v0.1 Machine Package

This package contains the machine-readable companion files for the SchemaFirst UTM Standard.

## Files

- `schemas/utm-standard.schema.json` — JSON Schema for the core UTM standard and organizational profiles.
- `schemas/utm-source.schema.json` — JSON Schema for canonical Source Registry records.
- `standards/utm/standard.json` — canonical SchemaFirst UTM v0.1 rules.
- `standards/utm/sources/*.json` — starter Source Registry records.

## Initial Source Registry

The starter registry intentionally covers a conservative set of common sources:

- Google
- Microsoft Bing
- LinkedIn
- Facebook
- Instagram
- Reddit
- YouTube
- Email
- SMS

Ambiguous or profile-dependent cases should be added deliberately rather than inferred.

## External basis

The defaults are grounded in current Google Analytics UTM and Default Channel Group guidance:

- https://support.google.com/analytics/answer/10917952
- https://support.google.com/analytics/answer/9756891
- https://support.google.com/analytics/answer/11242870
- https://support.google.com/analytics/answer/15612152

Google defines UTM semantics and channel behavior. SchemaFirst owns the stricter canonical values, deterministic campaign-slug rules, and organization-extension model.

## License

Apache License 2.0. See [LICENSE](LICENSE), [NOTICE](NOTICE), and [COMMERCIAL-LICENSE.md](COMMERCIAL-LICENSE.md).
