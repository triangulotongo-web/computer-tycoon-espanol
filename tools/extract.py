"""Extrae textos candidatos de Computer Tycoon: MonoBehaviours de data.unity3d y literales de global-metadata.dat."""
import UnityPy, struct, json, os, collections
D = r"C:\Program Files (x86)\Steam\steamapps\common\Computer Tycoon\Computer Tycoon_Data"
OUT = os.path.join(os.path.dirname(__file__), "..", "work")

def scan(raw):
    i, n = 0, len(raw)
    while i + 4 <= n:
        L = struct.unpack_from("<i", raw, i)[0]
        if 2 <= L <= 4000 and i + 4 + L <= n:
            try:
                s = raw[i+4:i+4+L].decode("utf-8")
                if s.isprintable() or "\n" in s:
                    yield s
                    i = (i + 4 + L + 3) & ~3; continue
            except UnicodeDecodeError:
                pass
        i += 4

assets = collections.Counter()
env = UnityPy.load(os.path.join(D, "data.unity3d"))
i2 = None
for o in env.objects:
    if o.type.name != "MonoBehaviour": continue
    try: raw = o.get_raw_data()
    except Exception: continue
    xs = list(scan(raw[28:]))
    if xs and xs[0] == "I2Languages": i2 = xs; continue
    for s in xs: assets[s] += 1
print("assets", len(assets))

m = open(os.path.join(D, r"il2cpp_data\Metadata\global-metadata.dat"), "rb").read()
_, ver, litOff, litSize, dataOff, _ = struct.unpack_from("<6I", m, 0)
code = set()
for k in range(litSize // 8):
    ln, idx = struct.unpack_from("<II", m, litOff + k*8)
    try: code.add(m[dataOff+idx: dataOff+idx+ln].decode("utf-8"))
    except UnicodeDecodeError: pass
json.dump(sorted(assets), open(os.path.join(OUT, "assets_raw.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
json.dump(sorted(code), open(os.path.join(OUT, "code_raw.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
json.dump(i2 or [], open(os.path.join(OUT, "i2_raw.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("code", len(code), "i2", len(i2 or []))
