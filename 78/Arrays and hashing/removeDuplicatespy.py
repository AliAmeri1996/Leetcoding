
"""remove duplicates from the list and return the number of elements in the new list"""
def removeDuplicates(nums): 
        if not nums:# this means if nums is empty
            return 0

        i = 0  # Last unique element index,this is our first pointer

        for j in range(1, len(nums)):# j is our next pointer
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                
        return i + 1
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

#i = 0  # Last unique element index

"""Initialize pointer i to 0.
Think of i as:
"the index of the last unique element we have seen so far."
We start at index 0 because the first element is always unique."""



# for j in range(1, len(nums)):
"""Loop over j starting at index 1.
j is a pointer that scans the rest of the array.
You start at 1 because you already considered nums[0] unique."""


#if nums[j] != nums[i]:
"""Compare the current value nums[j] with the last unique value nums[i].
If they are different, you have found a new unique element."""



# i += 1
"""Move the i pointer forward by 1.
This means:
"I found a new unique element, so I need to reserve the next slot to store it."""

#nums[i] = nums[j]
"""nums[j] را در nums[i] کپی می‌کنیم تا مقدار یکتا در همان آرایه ذخیره شود
 (بدون ایجاد آرایه جدید)."""

#  return i + 1
"""After the loop:

i is the index of the last unique element.

The count of unique elements = i + 1 (because index starts at 0)."""
