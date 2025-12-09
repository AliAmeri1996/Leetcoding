"""removes the elements that are similar to val and returns the number of newly
formed array"""

def removeElement( nums, val):
        i = 0  # i is our first pointer
        for j in range(len(nums)):# j is our other pointer
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
#j: Scans every element in the array (0 to n-1).

#i: Marks the position where you write the next element you want to keep.            
         

print(removeElement([0,1,2,2,3,0,4,2], val = 2))


#if nums[j] != val:
"""If the current element is not equal to
 val (i.e., this is a value you want to keep)..."""


#nums[i] = nums[j]
""""Copy this element into position i."

This moves the valid element forward in the array.

It overwrites any unwanted value that was there before.

In effect, it “compacts” all the good values to the front."""
#It copies valid elements to the front of the array, one by one.


#i += 1
"""Move i forward to be ready for the next valid element."""

#return i
"""Meaning in plain English:
👉 i is the count of elements you kept (i.e., elements that are not equal to val)."""
#Remember this part of your code:
"""i = 0
You started with i=0 (no elements written yet).

Then, each time you find a value you want to keep, you do:

nums[i] = nums[j]
i += 1

This moves i forward by 1.

So at the end:

i is how many times you copied something in.

That’s exactly the new length of your array after removing val



"""

