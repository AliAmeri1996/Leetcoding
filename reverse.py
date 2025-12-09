# #The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:

# #Input
# #Expected output
# 4
# #Animals Bugs
# Dobsonflies Hellgrammites
# Corydalidae Dobsonflies
# Bugs Corydalidae

# Animals
# Bugs
# Corydalidae
# Dobsonflies
# Hellgrammites


d={}
for _ in range(int(input())):
    a,b=input().split()
    d[a]=b

s=list(set(d.keys()) - set(d.values()))[0]
while s:
    print(s)
    s = d.get(s,None)