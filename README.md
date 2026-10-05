# SchemaFirst UTM Standard

Deterministic rules for generating UTM parameters. Given the same campaign, source, and distribution context, two conforming agents generate the same UTM.

- Website: [www.schemafirst.org/standards/utm](https://www.schemafirst.org/standards/utm)
- Standard: [`standards/utm/standard.json`](standards/utm/standard.json)
- Source Registry: [`standards/utm/sources/`](standards/utm/sources/)
- Schemas: [`schemas/utm-standard.schema.json`](schemas/utm-standard.schema.json), [`schemas/utm-source.schema.json`](schemas/utm-source.schema.json)
- Conformance cases: [`cases/`](cases/)

## Version 0.2.0 (draft)

0.2.0 adopts the naming shared by all SchemaFirst standards: kebab-case for SchemaFirst keys and values. Generation behavior is unchanged from 0.1.0; names are not.

| 0.1.0 | 0.2.0 |
| --- | --- |
| `distribution_context`, `destination_url`, `campaign_id`, … | `distribution-context`, `destination-url`, `campaign-id`, … |
| `requires_context`, `unknown_source`, `unsupported_context` | `requires-context`, `unknown-source`, `unsupported-context` |
| `standard_version` | `standard-version` |
| `canonical_source`, `display_name`, `registry_version` | `canonical-source`, `display-name`, `registry-version` |
| `google_defined`, `schemafirst_default` | `google-defined`, `schemafirst-default` |
| provenance class `organization_override_permitted` | `organization-defined` (whether a value may be replaced stays in `overridable`) |
| requirement `recommended_where_applicable` | requirement `recommended` with `applies-when` |

Unchanged, because Google Analytics defines them: the parameter names (`utm_source`, `utm_medium`, …) wherever they appear, including as keys. Unchanged, because they are emitted data: campaign slugs (`spring_product_launch`), mediums (`paid_social`), and aliases.

## Conformance

A conforming implementation produces exactly the `expected` output for every file in `cases/`. The reference generator checks them:

```bash
python3 scripts/check-conformance.py
```

## Source Registry

The starter registry covers Google, Microsoft Bing, LinkedIn, Facebook, Instagram, Reddit, YouTube, Email, and SMS. Each record is its own file so changes are reviewed individually. Ambiguous or profile-dependent cases are added deliberately, not inferred. The registry is versioned independently of the standard.

## External basis

Google defines UTM semantics and channel behavior. SchemaFirst owns the stricter canonical values, deterministic campaign-slug rules, and organization-profile model.

- https://support.google.com/analytics/answer/10917952
- https://support.google.com/analytics/answer/9756891
- https://support.google.com/analytics/answer/11242870
- https://support.google.com/analytics/answer/15612152

SchemaFirst is an independent community standard. It is not authored or endorsed by Google.

## License

Apache License 2.0. See [LICENSE](LICENSE), [NOTICE](NOTICE), and [COMMERCIAL-LICENSE.md](COMMERCIAL-LICENSE.md).
