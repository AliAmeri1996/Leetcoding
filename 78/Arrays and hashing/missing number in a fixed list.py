'''how to find the missing number in a given interger array of 1 to 100'''

nums = [1, 2, 3, 4, 5, 6, 8, 9, 10]  # 7 is missing

def find_missing_number(nums):
    n = 10
    expected_sum = n * (n + 1) // 2  #  the sum of numbers from 1 to 1055
    actual_sum = sum(nums)           # 48
    return expected_sum - actual_sum # 7

print(find_missing_number(nums))