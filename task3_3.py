"""Task 3.3 — Recursive Diff & Merge with Conflict Detection"""

import copy, random


def diff(old, new, path=""):
    result = {}
    for k in set(old) | set(new):
        p = f"{path}.{k}" if path else k
        o, n = old.get(k), new.get(k)
        if isinstance(o, dict) and isinstance(n, dict):
            result.update(diff(o, n, p))
        elif o != n:
            result[p] = (o, n)
    return result


def _set(d, path, val):
    for k in path[:-1]:
        d = d.setdefault(k, {})
    if val is None: d.pop(path[-1], None)
    else:           d[path[-1]] = val


def merge(base, v1, v2):
    da, db   = diff(base, v1), diff(base, v2)
    result   = copy.deepcopy(base)
    conflicts = []
    for p in set(da) | set(db):
        a, b = da.get(p, (None, None))[1], db.get(p, (None, None))[1]
        if p in da and p in db and a != b:
            conflicts.append(f"CONFLICT '{p}': A→{a!r} vs B→{b!r}")
        else:
            _set(result, p.split("."), a if p in da else b)
    return result, conflicts


# ── Test A: manual example ────────────────────────────────────────────

V0 = {"system": {"network": {"ip": "192.168.1.1", "dns": "8.8.8.8"},
                  "display": {"brightness": 70, "theme": "light"}},
      "user":   {"name": "Admin", "role": "root"}}

V1 = copy.deepcopy(V0)
V1["system"]["display"]["brightness"] = 90
V1["user"]["role"] = "superadmin"

V2 = copy.deepcopy(V0)
V2["system"]["display"]["theme"]      = "dark"
V2["system"]["network"]["dns"]        = "1.1.1.1"
V2["system"]["display"]["brightness"] = 50      # conflict with V1

print("── diff V0→V1:", diff(V0, V1))
print("── diff V0→V2:", diff(V0, V2))
merged, conflicts = merge(V0, V1, V2)
print("── conflicts: ", conflicts)
print("── merged:    ", merged)


# ── Test B: no conflicts (from task spec) ─────────────────────────────

V0b = {"display": {"brightness": 70, "color": "warm"}}
V1b = copy.deepcopy(V0b); V1b["display"]["brightness"] = 80
V2b = copy.deepcopy(V0b); V2b["display"]["color"] = "cold"

mb, cb = merge(V0b, V1b, V2b)
print("\n── Test B merged:", mb, "| conflicts:", cb)
print("── expected:     {'display': {'brightness': 80, 'color': 'cold'}}")


# ── Test C: stress test (depth=5) ─────────────────────────────────────

def _rand_path(d, p=None):
    p = p or []
    return _rand_path(d[k := random.choice(list(d))], p + [k]) if isinstance(d, dict) else p

def make_stress(depth=5, width=3):
    def gen(d): return random.randint(1,100) if d==0 else {f"node_{i}":gen(d-1) for i in range(width)}
    v0 = gen(depth)
    v1, v2 = copy.deepcopy(v0), copy.deepcopy(v0)
    for target, lo, hi in [(v1,1000,2000),(v1,1000,2000),(v1,1000,2000),
                            (v2,3000,4000),(v2,3000,4000),(v2,3000,4000)]:
        _set(target, _rand_path(v0), random.randint(lo, hi))
    return v0, v1, v2

v0, v1, v2 = make_stress()
da, db = diff(v0, v1), diff(v0, v2)
_, cc  = merge(v0, v1, v2)

print(f"\n── Test C (depth=5): A changed {len(da)}, B changed {len(db)}, conflicts: {len(cc)}")
for p, (o, n) in da.items(): print(f"   A  {p}: {o} → {n}")
for p, (o, n) in db.items(): print(f"   B  {p}: {o} → {n}")
for c in cc:                  print(f"   ⚠  {c}")