def is_palindrome(s: str) -> bool:
    cleaned = ''.join([i.lower() for i in s if i.isalnum()])
    return cleaned == cleaned[::-1]


#O(n)