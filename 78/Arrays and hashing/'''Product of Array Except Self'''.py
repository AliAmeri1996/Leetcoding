'''Product of Array Except Self'''


def product_except_self_bruteforce(nums):
    n = len(nums)
    answer = []
    for i in range(n):
        product = 1 #You initialize product = 1 inside the outer loop so it RESETS for each i. Each index needs its own product of “all elements except i”.
        for j in range(n):
            if i != j:# when i and j are not the same index
                product *= nums[j]#multiply all the js without the i
        answer.append(product)
    return answer


#if product+=1 was inside the j loop, it would times 1 to each element and dont multiply them to each other