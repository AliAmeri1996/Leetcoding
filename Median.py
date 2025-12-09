from statistics import median

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
s = list(map(int, input().split()))
u = sum(a for a in s if s.count(a) == 1)
print(int(u * median(s)))


