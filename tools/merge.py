"""Une work/out/*.txt en Translation/es/Text/ comprobando que cada original existe tal cual en el juego."""
import re, glob, os, json

def split(line):
    for m in re.finditer(r"(?<![\x5c])=", line):
        return line[:m.start()], line[m.end():]
    return None

def unesc(s):
    return re.sub(r"\x5c([nrt=\x5c])", lambda m: {"n": "\n", "r": "\r", "t": "\t", "=": "=", "\x5c": "\x5c"}[m.group(1)], s)

def esc(s):
    return s.replace("\x5c", "\x5c\x5c").replace("=", "\x5c=").replace("\r", "\x5cr").replace("\n", "\x5cn").replace("\t", "\x5ct")

def norm(s):
    # espacios duros y saltos de Windows no cuentan al buscar el original
    return re.sub(r"\s+", " ", s.replace("\xa0", " ")).strip()

orig = {}
for c in glob.glob("work/chunks/c*.json"):
    for s in json.load(open(c, encoding="utf-8")):
        orig.setdefault(s.strip(), s)
        orig.setdefault(s.replace("\r\n", "\n").strip(), s)
        orig.setdefault(norm(s), s)

seen, lit, rx, bad, fixed = set(), [], [], [], 0
for f in sorted(glob.glob("work/out/c*.txt")):
    for line in open(f, encoding="utf-8-sig"):
        line = line.rstrip("\r\n")
        if not line.strip(): continue
        p = split(line)
        if not p or not p[1].strip(): bad.append((f, line)); continue
        k, v = p
        # las siglas de puntos se quedan como en la interfaz del juego
        v = re.sub(r"\bPI\b", "RP", v); v = re.sub(r"\bPL\b", "LP", v); v = re.sub(r"\bPPG\b", "SPP", v)
        if k.startswith(("r:", "sr:")):
            m = re.fullmatch(r'(s?r):"(.*)"', k)
            try: re.compile(m.group(2))
            except Exception: bad.append((f, line)); continue
            if k not in seen: seen.add(k); rx.append(line)
            continue
        raw = unesc(k)
        o = orig.get(raw.strip()) or orig.get(raw.replace("\r\n", "\n").strip()) or orig.get(norm(raw))
        if o is None: bad.append((f, line)); continue
        key = esc(o.strip())
        if key != k: fixed += 1
        if key in seen or unesc(v).strip() == o.strip(): continue
        seen.add(key); lit.append(key + "=" + v)

os.makedirs("Translation/es/Text", exist_ok=True)
open("Translation/es/Text/ComputerTycoon_es.txt", "w", encoding="utf-8", newline="\n").write("\n".join(lit) + "\n")
open("Translation/es/Text/ComputerTycoon_es_regex.txt", "w", encoding="utf-8", newline="\n").write("\n".join(rx) + "\n")
print("literales", len(lit), "regex", len(rx), "claves corregidas", fixed, "descartadas", len(bad))
for b in bad[:20]: print("  ", b[0][-6:], b[1][:120])
