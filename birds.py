#The Birds Language has only one rule: after each vowel (a,e,i,o,u,A,E,I,O,U) 
#you should insert the letter p followed by the vowel one more time. 
#For a given string convert it to Birds Language.



string = input()
vowels = ['a','e','i','o','u','A','E','I','O','U']
birds = ""
for ch in string:
    if ch in vowels:
        birds += ch + "p" + ch
    else:
        birds += ch


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(birds)