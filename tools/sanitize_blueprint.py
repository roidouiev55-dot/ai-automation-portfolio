"""Strip secrets and account-specific IDs from Make blueprints / n8n workflow exports
before committing them to a public repo.

Usage: python tools/sanitize_blueprint.py input.json output.json
"""
import json, re, sys

SENSITIVE_KEYS = {"__IMTCONN__", "__IMTHOOK__", "credentials", "webhookId", "chat_id", "chatId",
                  "base", "table", "apiKey", "api_key", "token", "accessToken", "password"}
PATTERNS = [
    (re.compile(r"app[A-Za-z0-9]{14}"), "<airtable_base>"),
    (re.compile(r"tbl[A-Za-z0-9]{14}"), "<airtable_table>"),
    (re.compile(r"res\.cloudinary\.com/[^/]+/"), "res.cloudinary.com/<cloud>/"),
    (re.compile(r"\b\d{9,12}:[A-Za-z0-9_-]{30,}\b"), "<telegram_bot_token>"),
    (re.compile(r"\b(sk|pk)-[A-Za-z0-9_-]{16,}"), "<api_key>"),
    (re.compile(r"EAA[A-Za-z0-9]{20,}"), "<meta_token>"),
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"), "<email>"),
]

def clean(v, key=None):
    if key in SENSITIVE_KEYS:
        return "<redacted>"
    if isinstance(v, dict):
        return {k: clean(x, k) for k, x in v.items()}
    if isinstance(v, list):
        return [clean(x) for x in v]
    if isinstance(v, str):
        for rx, rep in PATTERNS:
            v = rx.sub(rep, v)
    return v

src, dst = sys.argv[1], sys.argv[2]
data = json.load(open(src, encoding="utf-8"))
json.dump(clean(data), open(dst, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("sanitized ->", dst)
