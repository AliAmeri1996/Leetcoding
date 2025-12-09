"""Given two strings needle and haystack, return the index of the first occurrence of needle in 
haystack, or -1 if needle is not part of haystack."""

def strStr(haystack, needle):
        n = len(haystack)
        m = len(needle)

        if m == 0:
            return 0

        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        return -1

#for i in range(n - m + 1):
"""Loop over all possible starting indices in haystack where needle could fit:
range(n - m + 1) generates indices from 0 to n - m.
We use n - m + 1 because the last valid start index is at position n - m."""

#if haystack[i:i + m] == needle:
"""“Give me the substring that starts at position i and has length m.”"""
#string[start : end]
"""It extracts a substring starting at index start and ending before index end."""   
#return -1    
"""If the loop completes without finding any match, return -1 to indicate needle does not occur in haystack."""