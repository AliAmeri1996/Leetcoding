
def lengthOfLongestSubstring(s):
        
      n = len(s)
      best_len = 0
      best = "" #It initializes the variable best as an empty string.
      for i in range(n):
         seen = set()
         for j in range(i, n):
             if s[j] in seen:
                 break
             seen.add(s[j])
#j = 0 → s[j] = 'a', not in seen → add it → substring = "a"
# j = 1 → s[j] = 'b', not in seen → add it → substring = "ab"
# j = 2 → s[j] = 'c', not in seen → add it → substring = "abc"
# j = 3 → s[j] = 'a', but 'a' is already in seen → 🚨 break!

             if j - i + 1 > best_len:#That’s the formula for the length of the current substring:
                 best_len = j - i + 1
                 #“If the length of the current substring is bigger than     the  longest one we’ve found so far…” 
                 best = s[i:j+1]#"Save the actual substring we just found, since it’s the longest so far."
      return len(best),best  # or return best_len if you just want the length

    

print(lengthOfLongestSubstring("aaabc"))




        # count = 0
        # n = len(s)
        # for i in range(n):
        #     seen = set()
        #     for j in range(i,n):
        #         if s[j] in seen:
        #             break
        #         seen.add(s[j])
        #     count = max(count,len(seen))
        # return count 