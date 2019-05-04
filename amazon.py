file = [
    ["user1", "canonT2i.html"],
    ["user2", "nikonD5000.html"],
    ["user1", "tripod.html"],
    ["user3", "canonT2i.html"],
    ["user4", "canonT2i.html"],
    ["user5", "nikonD5000.html"],
    ["user2", "tripod.html"],
    ["user3", "tripod.html"],
    ["user4", "nikonD5000.html"],
    ["user4", "tripod.html"],
]

def parsed_lines(file):
    for l in file:
        yield l[0], l[1]

def rank_seq():
    users = {}
    all_seq = []
    for u, page in parsed_lines(file):
        print(u, page)
        if u in users.keys():
            all_seq.append((users[u], page))
            users[u] = page
        else:
            users[u] = page
    print(all_seq)
    s = set(all_seq)
    results = {}
    results = {r: all_seq.count(r) for r in s}
    return results

print(rank_seq())
