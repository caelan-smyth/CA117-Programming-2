def build_dictionary(filename):
    d = {}
    with open(filename, 'r') as f:
        for line in f:
            k, v = line.strip().split()
            d[k] = int(v)
    return d


def extract_range(d, low, high):
    new_d = {}
    for t in d.items():
        if low <= t[1] <= high:
            new_d[t[0]] = t[1]
    return new_d