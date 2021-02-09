import asyncio

async def line(filename):
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line: break
            yield int(line)

async def run(mx):
    files = [line(f"{i}.txt") for i in range(1,mx+1)]
    lines = [await f.__anext__() for f in files]
    while True:
        m = min(lines)
        n = lines.index(m)
        print(m, ": ", n, lines)
        
        try:
            lines[n] = await files[n].__anext__()
        except StopAsyncIteration:
            lines[n] = 2**32
        if all([l == 2**32 for l in lines]): break

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(run(4))
finally:
    loop.close()
