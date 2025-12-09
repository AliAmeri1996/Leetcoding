def palimdrom(s):
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

print(palimdrom(("")))

#if c.isalnum()
"""c.isalnum() checks whether c is alphanumeric (a letter or digit).
This filters out spaces, punctuation, and symbols."""

#''.join()
"""he generator expression inside join() produces a sequence of cleaned characters.
''.join(...) concatenates them all into a single string with no separator."""




#if c.isalnum(): keep only alphanumeric characters (ignores spaces, punctuation, etc.)
#''.join(...): combines the cleaned characters into one single string