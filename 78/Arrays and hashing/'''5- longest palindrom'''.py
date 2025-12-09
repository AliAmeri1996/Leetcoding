'''5- longest palindrom'''
'''Given a string s, return the longest palindromic substring in s.'''


def longestPalindrome(s):
    longest = ""# initilizing the string we want, cause remeber we want a string, thats the end goal
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) > len(longest):# this is also the method to find the longest in basically anything
                longest = sub
    return longest
