import UnityPy, struct
D = r"C:\Program Files (x86)\Steam\steamapps\common\Computer Tycoon\Computer Tycoon_Data"
env = UnityPy.load(D + r"\data.unity3d")
scripts = {}
for o in env.objects:
    if o.type.name == "MonoScript":
        d = o.read(); scripts[(o.assets_file.name, o.path_id)] = d.m_ClassName
hits = 0
for o in env.objects:
    if o.type.name != "MonoBehaviour": continue
    raw = o.get_raw_data()
    if len(raw) < 20000: continue
    if b"Spanish" in raw or b"English" in raw:
        print(o.assets_file.name, o.path_id, len(raw), raw.count(b"Spanish"), raw.count(b"English"))
        hits += 1
m = open(D + r"\il2cpp_data\Metadata\global-metadata.dat","rb").read(8); print("metadata v", struct.unpack("<II", m)[1])
