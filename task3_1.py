"""Task 3.1 — Buyer Similarity (Cosine)"""

import math, random, time


def similarity(storage, a, b):
    pa, pb = storage.get(a, {}), storage.get(b, {})
    if len(pa) > len(pb):
        pa, pb = pb, pa
    dot = sum(v * pb[k] for k, v in pa.items() if k in pb)
    if not dot:
        return 0.0
    norm = lambda p: math.sqrt(sum(v**2 for v in p.values()))
    return dot / (norm(pa) * norm(pb))


def update(storage, user, item, delta):
    p = storage.setdefault(user, {})
    p[item] = p.get(item, 0) + delta
    if p[item] <= 0:
        del p[item]


# ── Tests ─────────────────────────────────────────────────────────────

db = {
    "u1": {"iPhone": 1, "AirPods": 1},
    "u2": {"iPhone": 1, "MacBook": 1},
    "u3": {"Keyboard": 3, "Mouse": 2},
    "u4": {"iPhone": 1, "AirPods": 1},
}

print("u1 vs u2 (exp 0.5):", round(similarity(db, "u1", "u2"), 4))
print("u1 vs u3 (exp 0.0):", round(similarity(db, "u1", "u3"), 4))
print("u1 vs u4 (exp 1.0):", round(similarity(db, "u1", "u4"), 4))
print("u1 vs u1 (exp 1.0):", round(similarity(db, "u1", "u1"), 4))

t = {"u": {"apple": 2, "banana": 1}}
update(t, "u", "banana", -1)
update(t, "u", "apple",  -1)
print("update   (exp {'apple':1}):", t["u"])


# ── Performance ───────────────────────────────────────────────────────

def make_data(n):
    catalog = [f"{b} {c} {i}" for b in ["Apple", "Samsung", "Sony", "Dell"]
               for c in ["Laptop", "Phone", "Watch"] for i in range(10)]
    return {f"u{i}": {k: random.randint(1, 5) for k in random.sample(catalog, random.randint(3, 10))}
            for i in range(n)}

print(f"\n{'Users':<12} {'µs / pair'}")
print("─" * 24)
for n in [100, 10_000, 1_000_000]:
    data  = make_data(n)
    users = list(data)
    pairs = [(random.choice(users), random.choice(users)) for _ in range(100)]
    t0 = time.perf_counter()
    for a, b in pairs:
        similarity(data, a, b)
    print(f"{n:<12} {(time.perf_counter()-t0)/100*1e6:.2f}")

print("\nO(1) profile lookup via dict — time scales with profile size, not user count.")