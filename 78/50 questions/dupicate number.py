def duplicate(n1):
    all=[]
    n=len(n1)
    for i in range(n):
        for j in range(i+1,n):# start from i+1 to avoid same index
            if n1[i]==n1[j]:
                all.append(n1[i])
                i+=1

        return all

print(duplicate([1,2,1,2]))
#O(n^2)



# def duplicate(n1):
#     seen = set()
#     for num in n1:
#         if num in seen:
#             return num
#         seen.add(num)
#O(n)


# def find_duplicate(nums):
#     nums.sort()
#     for i in range(1, len(nums)):
#         if nums[i] == nums[i - 1]:
#             return nums[i]
#     return None

# print(find_duplicate([1, 3, 4, 2, 2])) 
#O(nlogn)