T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    harvest_schedule = []
    for _ in range(N):
        s, e = map(int, input().split())
        harvest_schedule.append((s,e))
    harvest_schedule = sorted(harvest_schedule)
    robots = 0
    duty_end = 0
    for start, end in harvest_schedule:
        if duty_end >= end:
            continue
        if duty_end >= start:
            start = duty_end
        harvest_interval = end - start
        robots_required = -(-harvest_interval // K)
        robots += robots_required
        duty_end = start + robots_required * K
    print("Case #{}: {}".format(t, robots))
