def generate_arrays(sizes, kind="random"):
    arrays = {}
    for n in sizes:
        if kind == "random":
            arrays[n] = [random.randint(0, 10**6) for _ in range(n)]
        elif kind == "sorted":
            arrays[n] = list(range(n))
        elif kind == "reversed":
            arrays[n] = list(range(n, 0, -1))
        elif kind == "almost_sorted":
            base = list(range(n))
            # Робимо кілька випадкових перестановок
            for _ in range(max(1, n // 100)):
                i, j = random.randrange(n), random.randrange(n)
                base[i], base[j] = base[j], base[i]
            arrays[n] = base
    return arrays