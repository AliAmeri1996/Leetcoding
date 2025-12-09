'''First Unique Character in a String'''
def firstUniqChar(s):
    unique={}
    for char in s:
        unique[char]=unique.get(char,0)+1

    for idx, char in enumerate(s):
        if unique[char] == 1:
            return idx
        
    return -1


#for idx, char in enumerate(s):
'''In Python, enumerate(s) is a built-in function that lets you loop through both: index and character like the follwing
0 l
1 o
2 v
3 e ''' 

print(firstUniqChar("leetcode"))

'''O(n)'''
