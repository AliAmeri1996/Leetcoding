def climb_stairs(n):
    if n == 0 or n == 1:
        return 1

    a, b = 1, 1  # ways(0), ways(1)
    for _ in range(2, n + 1):
        a, b = b, a + b  # a becomes ways(n-2), b becomes ways(n-1) → b = ways(n)
    
    return b


print(climb_stairs(3))