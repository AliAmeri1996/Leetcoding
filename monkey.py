n = int(input("number of monkies?"))
day = input("what day is it?")
funkiness = float(input("whats the level of funckiness?"))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

r = []
for _ in range(n):
    if day == "friday":
        r.append("funky monkey friday")
    else:
        r.append("monkey")

s = " ".join(r) # this give spaces between the words written

if funkiness >=7:
    s = s.upper()
print(s)