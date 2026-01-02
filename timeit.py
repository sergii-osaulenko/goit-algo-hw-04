import csv

sizes = [100, 1000, 5000]
kinds = ["random", "sorted", "reversed", "almost_sorted"]

results = []

for kind in kinds:
    arrays = generate_arrays(sizes, kind)
    for n in sizes:
        arr = arrays[n]
        for algo_name, func in [
            ("insertion", insertion_sort),
            ("merge", merge_sort),
            ("timsort", timsort),
        ]:
            t = timeit.timeit(lambda: func(arr), number=5)
            results.append((kind, n, algo_name, t))

# зберігаємо результати в CSV, щоб легко аналізувати й будувати таблиці/графіки
with open("sorting_benchmark.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["data_type", "n", "algorithm", "time_sec_5_runs"])
    writer.writerows(results)