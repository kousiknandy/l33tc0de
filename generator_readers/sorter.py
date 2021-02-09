def line(filename):
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line: break
            yield int(line)

def run(mx):
    files = [line(f"{i}.txt") for i in range(1,mx+1)]
    lines = [next(f) for f in files]
    while True:
        m = min(lines)
        n = lines.index(m)
        print(m, ": ", n, lines)
        try:
            lines[n] = next(files[n])
        except StopIteration:
            lines[n] = 2**32
        if all([l == 2**32 for l in lines]): break

run(4)
