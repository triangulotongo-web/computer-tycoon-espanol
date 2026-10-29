"""Segundo filtro, suave: solo quita mensajes de .NET/Unity y logs evidentes (en este juego 'server', 'memory'... son contenido)."""
import json, re
BAD = re.compile(r"(exception|\bnull\b|\bparse|serializ|socket|\bRSA\b|\bxml|\bjson|regex|constructor|argument|assembly|attribute|\bencoding|\buri\b|https?|\bthread|async|delegate|\benum\b|\bstruct\b|namespace|vertex|vertices|glyph|font asset|sprite|canvas|animator|navmesh|collider|rigidbody|gameobject|prefab|\bguid\b|il2cpp|\bmono\b|unity|deprecated|obsolete|\binvalid\b|must be|must not|should not|cannot be|could not|not supported|is not a valid|\bbuffer\b|\bstream\b|\bpointer\b|\bmethod\b|\bproperty\b|\bparameter\b|\bnode\b|\bindex\b|out of range|\btypeof\b|\bdebug\b|\bassert\b|steamworks|\bshader\b|\btexture\b|\bmesh\b|\bmaterial\b|\bcomponent\b(?= (is|was|of type))|addressable|\bbundle\b|\bpacket\b|\bcallback\b|\bfail(ed)? to\b|\bunable to\b)", re.I)
LOCALE = re.compile(r"^[A-Z][a-z]+( [A-Z][a-z]+)? \([^)]*\)$")
xs = json.load(open("work/code_f.json", encoding="utf-8"))
keep = []
for s in xs:
    t = s.strip()
    if BAD.search(t) or LOCALE.match(t): continue
    if re.fullmatch(r"[a-z][a-z0-9\-]*", t): continue
    if re.fullmatch(r"[A-Z][A-Za-z0-9]+", t) and re.search(r"[a-z][A-Z]", t): continue
    if t.startswith("[") or t.startswith("<ds.") or t.startswith("_"): continue
    keep.append(s)
json.dump(keep, open("work/code_f2.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(keep))
