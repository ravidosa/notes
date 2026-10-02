import random

for a, b, u in [(1, 1, 0), (2, 2, 1), (3, 3, 4), (4, 1, 0), (7, 2, 1), (7, 1, 2), (5, 3, 2), (5, 2, 3)]:
    for e in range(1, 7):
        n = 10 ** e
        N = int(10 ** (3 - e / 2))
        a, b, u = a / (a + b + u), b / (a + b + u), u / (a + b + u)
        t_sum = 0
        for _ in range(N):
            counts = {"a": int(a * n), "b": int(b * n), "u": n - int(a * n) - int(b * n)} # lanterning it. and by it i mean my fish

            interactions = 0
            while counts["a"] != n and counts["b"] != n:
                rand = random.random()
                p4a = 0.5 * (counts["a"] * counts["b"] / n ** 2)
                p4b = p4a + 0.5 * (counts["a"] * counts["b"] / n ** 2)
                p4c = p4b + (counts["a"] * counts["u"] / n ** 2)
                p4d = p4c + (counts["b"] * counts["u"] / n ** 2)
                if rand < p4a:
                    counts["b"] -= 1
                    counts["u"] += 1
                elif p4a <= rand < p4b:
                    counts["a"] -= 1
                    counts["u"] += 1
                elif p4b <= rand < p4c:
                    counts["a"] += 1
                    counts["u"] -= 1
                elif p4c <= rand < p4d:
                    counts["b"] += 1
                    counts["u"] -= 1
                interactions += 1
            t_sum += interactions / n
        print("(" + str(e) + "," + str(t_sum / N) + ")")
    print()
        