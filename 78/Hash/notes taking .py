'''It must print Yes  if the note can be formed using the magazine, or No'''


def checkMagazine(magazine, note):
    word_count = {}
    
    # Count magazine words
    for word in magazine:
        word_count[word] = word_count.get(word, 0) + 1
    
    # Check note words
    for word in note:
        if word_count.get(word, 0) == 0:
            print("No")
            return
        word_count[word] -= 1
    
    print("Yes")


print(checkMagazine("give on give"))


#word_count[word] = word_count.get(word, 0) + 1
# basically this checks the key of the dic and counts the number of occurance       
'''
Use the word as the key in the dictionary,
and store the number of times (occurrences) we’ve seen it as the value.
something like {"give": 1, "me": 1, "one": 1}
'''



#if word_count.get(word, 0) == 0
'''If this word isn’t in the dictionary (no key) OR it’s in the dictionary but its value is 0…”'''
