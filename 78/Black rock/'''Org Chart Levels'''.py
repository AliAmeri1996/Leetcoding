'''Org Chart Levels'''

import sys

def parse_pair(s):
    s = s.strip()
    if "/" in s:
        a, b = s.split("/", 1)
    else:
        p = s.split()
        a, b = p[0], p[1]
    return a.strip(), b.strip()

def build_manager_map(pairs):
    m = {}
    for emp, mgr in pairs:
        m[emp] = mgr
    return m

def chain_up(name, mgr_map):
    chain = []
    seen = set()
    cur = name
    while cur in mgr_map and cur not in seen:
        nxt = mgr_map[cur]
        chain.append(nxt)
        seen.add(cur)
        cur = nxt
    return chain

def levels_between(a, b, pairs):
    if a == b:
        return 0
    mgr_map = build_manager_map(pairs)
    path_a = chain_up(a, mgr_map)
    path_b = chain_up(b, mgr_map)

    # if b is above a
    if b in path_a:
        return path_a.index(b) + 1
    # if a is above b
    if a in path_b:
        return path_b.index(a) + 1
    # not connected
    return 0

def main():
    lines = [ln.strip() for ln in sys.stdin if ln.strip()]
    if not lines:
        print(0)
        return

    name1, name2 = parse_pair(lines[0])
    pairs = [parse_pair(ln) for ln in lines[1:] if ln]
    print(levels_between(name1, name2, pairs))

if __name__ == "__main__":
    main()
