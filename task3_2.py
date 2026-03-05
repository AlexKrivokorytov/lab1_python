"""Task 3.2 — Full-Text Search (Inverted Index)"""

import re, time, random, datetime
from collections import defaultdict


# ── Build index ───────────────────────────────────────────────────────

def build_index(logs):
    idx = {f: defaultdict(set) for f in ("message", "level", "service", "trace_id")}
    idx["_logs"] = {}
    for log in logs:
        i = log["id"]
        idx["_logs"][i] = log
        for token in re.findall(r"[a-z0-9\-]+", log["message"].lower()):
            idx["message"][token].add(i)
        for field in ("level", "service", "trace_id"):
            idx[field][log[field]].add(i)
    return idx


# ── Search ────────────────────────────────────────────────────────────

def search(idx, **filters):
    sets = []
    for field, value in filters.items():
        if field == "message":
            tokens = re.findall(r"[a-z0-9\-]+", value.lower())
            s = idx["message"].get(tokens[0], set())
            for t in tokens[1:]:
                s &= idx["message"].get(t, set())
            sets.append(s)
        else:
            sets.append(idx[field].get(value, set()))
    ids = sets[0]
    for s in sets[1:]:
        ids &= s
    return [idx["_logs"][i] for i in ids]


# ── Demo ──────────────────────────────────────────────────────────────

logs = [
    {"id": 0, "trace_id": "TRC-101", "level": "ERROR", "service": "auth-gateway",      "message": "User login failed: invalid password."},
    {"id": 1, "trace_id": "TRC-102", "level": "ERROR", "service": "payment-processor", "message": "Payment failed: connection timeout."},
    {"id": 2, "trace_id": "TRC-103", "level": "INFO",  "service": "auth-gateway",      "message": "User login success."},
]
idx = build_index(logs)

print("index['message']:", dict(idx["message"]))
print('\nsearch "failed login":', [r["id"] for r in search(idx, message="failed login")])
print('search level=ERROR, service=auth-gateway:', [r["id"] for r in search(idx, level="ERROR", service="auth-gateway")])


# ── Performance ───────────────────────────────────────────────────────

def make_logs(n):
    svcs    = ["auth-gateway", "payment-processor", "inventory-db"]
    actions = ["connected to", "failed to process", "timed out during"]
    res     = ["database", "s3-bucket", "redis-cache"]
    traces  = [f"TRC-{i:06d}" for i in range(50000)]
    start   = datetime.datetime.now()
    return [{"id": i, "timestamp": (start + datetime.timedelta(milliseconds=i*10)).isoformat(),
             "level": random.choice(["INFO","DEBUG","WARNING","ERROR","CRITICAL"]),
             "service": random.choice(svcs), "trace_id": random.choice(traces),
             "message": f"Service {random.choice(svcs)} {random.choice(actions)} {random.choice(res)}"}
            for i in range(n)]

print(f"\n{'Logs':<12} {'Build(s)':<12} {'Linear(µs)':<14} {'Index(µs)':<12} {'Speedup'}")
print("─" * 58)

for n in [100, 10_000, 1_000_000]:
    data   = make_logs(n)
    t0     = time.perf_counter(); idx = build_index(data); build = time.perf_counter() - t0
    target = data[n // 2]["trace_id"]

    t0 = time.perf_counter()
    for _ in range(50): _ = [l for l in data if l["trace_id"] == target]
    linear = (time.perf_counter() - t0) / 50 * 1e6

    t0 = time.perf_counter()
    for _ in range(50): _ = [idx["_logs"][i] for i in idx["trace_id"].get(target, set())]
    indexed = (time.perf_counter() - t0) / 50 * 1e6

    print(f"{n:<12} {build:<12.4f} {linear:<14.2f} {indexed:<12.4f} {linear/indexed:.0f}x")

print("\nLinear O(N) grows with log count; index O(1) stays constant.")