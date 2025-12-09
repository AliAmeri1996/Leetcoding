'''Given an integer array nums, return an array output where output[i]
 is the product of all the elements of nums except nums[i].'''

def product(numbers):
    result = []
    for i in range(len(numbers)):
        prod = 1# everytime the numbers are getting multiplied in the list, youve got to
        #start from 1
        for j in range(len(numbers)):
            if i != j:
                prod *= numbers[j]
        result.append(prod)
    return result

# Example usage:
print(product([1, 2, 4, 6]))


'''We are inside two nested loops:

The outer loop:


for i in range(len(numbers)):
This picks each position i (the index of the number you want to exclude).

The inner loop:


for j in range(len(numbers)):
This loops over all indices to multiply them, except the one you are excluding.

✅ Line-by-line explanation:

1. if i != j:

This means:

Only do the multiplication if j (current index in the inner loop) is not equal to i (the index we are excluding).

In other words:

“Skip multiplying the number in position i.”

2. prod *= numbers[j]

This multiplies prod by the current number at position j.

Example:

If prod was 1 and numbers[j] is 2, then prod becomes 2.

Next time, if numbers[j] is 4, prod becomes 2 * 4 = 8.

By the end of the inner loop, prod is the product of all numbers except numbers[i].

3. result.append(prod)

Once we finish multiplying all the numbers except numbers[i], we append the resulting product to the result list.

This way, result ends up with one product for each position in the input list.

'''

  
    
        
