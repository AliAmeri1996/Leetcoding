'''is happy'''
import sys

def is_happy(n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        # compute sum of squares of digits
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if is_happy(n):
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    main()
