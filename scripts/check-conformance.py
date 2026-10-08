"""Reference generator for the SchemaFirst UTM Standard. Runs every case in cases/ and reports mismatches.

Usage: python3 scripts/check-conformance.py
"""
import glob
import json
import os
import re
import sys
import unicodedata
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STANDARD = json.load(open(os.path.join(ROOT, "standards/utm/standard.json")))
SOURCES = list(STANDARD["sources"].values())
OPTIONAL_INPUTS = {
    "utm_id": "campaign-id",
    "utm_source_platform": "source-platform",
    "utm_content": "content",
    "utm_term": "term",
    "utm_creative_format": "creative-format",
    "utm_marketing_tactic": "marketing-tactic",
}


def slug(text):
    text = "".join(c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def resolve(source):
    s = source.lower()
    for rec in SOURCES:
        if s == rec["canonical-source"] or s in (a.lower() for a in rec["aliases"]):
            return rec
    return None


def assemble(url, params):
    base, _, fragment = url.partition("#")
    path, _, query = base.partition("?")
    kept = [p for p in query.split("&") if p and not p.startswith("utm_")]
    order = STANDARD["url-assembly"]["parameter-order"]
    kept += [f"{k}={quote(params[k], safe='')}" for k in order if params.get(k)]
    out = path + ("?" + "&".join(kept) if kept else "")
    return out + ("#" + fragment if fragment else "")


def generate(inp):
    missing = [k for k in STANDARD["inputs"]["required"] if not inp.get(k)]
    campaign = inp.get("campaign") or {}
    if "campaign" not in missing and not (campaign.get("slug") or campaign.get("name")):
        missing.append("campaign")
    if missing:
        return {"status": "requires-context", "missing": missing}
    rec = resolve(inp["source"])
    if rec is None:
        return {"status": "unknown-source", "source": inp["source"]}
    ctx = rec["contexts"].get(inp["distribution-context"])
    if ctx is None:
        return {"status": "unsupported-context", "source": rec["canonical-source"], "supported": list(rec["contexts"])}
    params = {
        "utm_source": rec["canonical-source"],
        "utm_medium": ctx["utm_medium"],
        "utm_campaign": campaign.get("slug") or slug(campaign["name"]),
    }
    for param, key in OPTIONAL_INPUTS.items():
        if inp.get(key):
            params[param] = inp[key] if param == "utm_id" else slug(inp[key])
    out = {"status": "ok", "standard-version": STANDARD["version"], "parameters": params}
    if inp.get("destination-url"):
        out["url"] = assemble(inp["destination-url"], params)
    return out


failures = 0
for path in sorted(glob.glob(os.path.join(ROOT, "cases/*.json"))):
    case = json.load(open(path))
    got = generate(case["input"])
    ok = got == case["expected"]
    failures += not ok
    print(("PASS " if ok else "FAIL ") + os.path.basename(path))
    if not ok:
        print("  expected:", json.dumps(case["expected"]))
        print("  got:     ", json.dumps(got))
sys.exit(1 if failures else 0)
