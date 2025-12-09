'''Design an algorithm to encode a list of strings to a single string. 
The encoded string is then decoded back to the original list of strings.'''



class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        return ''.join(f'{len(s)}#{s}' for s in strs)
    '''3#cat5#hello0#"'''#it adds the strings and before each word it counts its length
  

    def decode(self, s):
        """Decodes a single string back to a list of strings."""
        res = []
        i = 0       #pointer
        while i < len(s):
                    # Find the delimiter '#'
            j = i   #j is another pointer
            while s[j] != '#':
                j += 1
                #this simply means while s[j] is not #, keep moving one point to the right
            length = int(s[i:j])
            j += 1  # skip the '#'
            res.append(s[j:j+length])
            i = j + length
        return res

#return ''.join(strs), this will glue all the strings in one

#i = 0,  i is a pointer to where we are in the encoded string s.

#while i < len(s):Loop as long as i has not reached the end of the string.

'''j = i
while s[j] != '#':
    j += 1
'''
#j starts at i and advances until it finds the #.
#This part finds where the # separator is in your encoded string so you can extract the length number that comes before it.



#s[i:j]
'''Give me the characters between positions i and j (not including j itself)'''
'''i by default is ZERO so the character zero to whatever j has reached'''

#s[j : j + length]
'''j is the start index (where the actual string begins, right after the #).

j + length is the end index (not included).

This slice extracts exactly length characters.
'''

#i = j + length

'''advance i to the start of the next encoded substring.'''


'''Suppose you have this encoded string:


s = "3#cat5#hello0#"
Recall positions:

arduino
Copy code
0: '3'
1: '#'
2: 'c'
3: 'a'
4: 't'
5: '5'
6: '#'
7: 'h'
...
First iteration:

You decoded "cat":

j = 2 (start of "cat")

length = 3

After taking s[2:5] = 'cat', you need to move past 'cat'.

✅ So:

ini
Copy code
i = j + length = 2 + 3 = 5
New i:

Points to s[5], which is '5' (the start of the next length).

'''