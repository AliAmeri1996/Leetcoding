

"""find the two positions of the two numbers that their sum matches the target, this is for a sorted list
of numbers"""
'''this only for sorted array'''


'''two pointer has been use
time: O(n)
space: O(1)'''



def twoSum(numbers, target):
    left=0
    right =len(numbers) - 1  # subtracting 1 gives the INDEX of the last element
    #because Python lists are 0-indexed

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return ([left, right]) # indicis are returned 
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    

print(twoSum([1,2,3,4],3))

# the indicis are ruterned 

#right =len(numbers) - 1

'''Example:
If numbers = [2, 7, 11, 15], then:

len(numbers) = 4

So, right = 4 - 1 = 3'''


#while left < right
'''This keeps the loop running as long as the two pointers haven't crossed each other.

You start with:

left = 0 (first element)

right = len(numbers) - 1 (last element)

If left == right, you're pointing at the same element, which is not allowed (you need two different numbers).

Once left > right, you've checked everything — time to stop.'''


#return [left + 1, right + 1]
'''this is used to bring back the index that starts from 1 rathar than 0'''




# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             return [i + 1, j + 1]
