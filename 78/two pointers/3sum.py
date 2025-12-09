'''You need to find all groups of three different numbers in the list that add up to 0.'''
def sum(nums):
    seen = set()          # set of tuples, automatically dedups, it could only hold immutable objects
    n = len(nums)

    for a in range(n):
        for b in range(a + 1, n):      # b > a ensures different indices
            for c in range(b + 1, n):  # c > b ensures different indices
                if nums[a] + nums[b] + nums[c] == 0:
                    triplet = tuple(sorted((nums[a], nums[b], nums[c])))#Tuples are immutable and hashable, so they can be stored in a set.
                    seen.add(triplet)
                    #removes the duplicate lists, so many of them 
                    # that are repeated would be eliminated

    return [list(t) for t in seen]
    #“for every tuple t in seen, turn it into a list.”
  

          
        
        

print(sum([-1,0,1,2,-1,-4]))





def threeSum(nums):
    nums.sort()   # must sort first for two-pointer logic
    result = []
    
    for i in range(len(nums) - 2):   # fix one number
        if i > 0 and nums[i] == nums[i-1]:
            continue  # skip duplicates
            
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # skip duplicates
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
                
            elif total < 0:
                left += 1
            else:
                right -= 1
                
    return result


#3Sum with two pointers → O(n^2) time, O(1) space.