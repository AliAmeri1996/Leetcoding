'''Given a string s, find the length of the longest substring without repeating characters.'''

def length_of_longest_substring(s: str) -> int:
    last = {}           # char -> last seen index
    left = 0            # left edge of current window
    best = 0

    for right, ch in enumerate(s):# the index of the charachter
        if ch in last and last[ch] >= left:#“Is the last time we saw this character still inside (or touching) the current window?”
            # ch repeats inside current window; move left past old ch
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)

    return best

print(length_of_longest_substring(s ="abcabcbb"))