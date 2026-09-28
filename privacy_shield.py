"""Privacy Shield: masks sensitive identifiers locally, before display, storage or speech.

Runs on the CPU with no network access. Aadhaar candidates are validated with the
Verhoeff checksum so random 12-digit numbers are not masked unnecessarily.
"""
import re

_D = [[0,1,2,3,4,5,6,7,8,9],[1,2,3,4,0,6,7,8,9,5],[2,3,4,0,1,7,8,9,5,6],[3,4,0,1,2,8,9,5,6,7],
      [4,0,1,2,3,9,5,6,7,8],[5,9,8,7,6,0,4,3,2,1],[6,5,9,8,7,1,0,4,3,2],[7,6,5,9,8,2,1,0,4,3],
      [8,7,6,5,9,3,2,1,0,4],[9,8,7,6,5,4,3,2,1,0]]
_P = [[0,1,2,3,4,5,6,7,8,9],[1,5,7,6,2,8,3,0,9,4],[5,8,0,3,7,9,6,1,4,2],[8,9,1,6,0,4,3,5,2,7],
      [9,4,5,3,1,2,6,8,7,0],[4,2,8,6,5,7,3,9,0,1],[2,7,9,3,8,0,6,4,1,5],[7,0,4,6,9,1,3,2,5,8]]


def verhoeff_valid(number: str) -> bool:
    c = 0
    for i, ch in enumerate(reversed(number)):
        c = _D[c][_P[i % 8][int(ch)]]
    return c == 0


AADHAAR_RE = re.compile(r"(?<!\d)(\d{4}[ -]?\d{4}[ -]?\d{4})(?!\d)")
PAN_RE = re.compile(r"\b[A-Z]{5}\d{4}[A-Z]\b")
PHONE_RE = re.compile(r"(?<!\d)(?:\+91[ -]?)?[6-9]\d{9}(?!\d)")
ACCOUNT_RE = re.compile(r"(?<!\d)\d{9,18}(?!\d)")


def _mask(value: str, keep: int = 4) -> str:
    chars = [c for c in value if c.isalnum()]
    return "X" * max(len(chars) - keep, 0) + "".join(chars[-keep:])


def mask_pii(text: str):
    """Return (masked_text, list_of_categories_found)."""
    found = []

    def aadhaar(m):
        raw = re.sub(r"[ -]", "", m.group(1))
        if verhoeff_valid(raw):
            found.append("aadhaar")
            return _mask(raw)
        return m.group(0)

    def simple(kind):
        def repl(m):
            if "X" in m.group(0):
                return m.group(0)
            found.append(kind)
            return _mask(m.group(0))
        return repl

    text = AADHAAR_RE.sub(aadhaar, text)
    text = PAN_RE.sub(simple("pan"), text)
    text = PHONE_RE.sub(simple("phone"), text)
    text = ACCOUNT_RE.sub(simple("account"), text)
    return text, found
