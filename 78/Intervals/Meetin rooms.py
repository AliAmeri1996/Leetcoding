def interval(n):
    # Sort intervals based on start time
    n.sort(key=lambda x: x[0])
    
    for i in range(1, len(n)):
        prev_start, prev_end = n[i - 1]
        curr_start, curr_end = n[i]

        # Check for overlap: if current meeting starts before previous one ends
        if curr_start < prev_end:
            print("false")
            return
    print("true")

print(interval([(5,8),(9,15)]
))


# n.sort(key=lambda x: x[0])

""" n.sort(key=lambda x: x[0]) this code says the following: """

"""this part is telling Python how to sort the items.

lambda x: x[0]

It means: “for each item x in the list, use x[0] as the sorting key.”
x represents each item in the list (x will be a tuple like (5, 10)
x[0] means: "take the first element of the tuple."
In our case, x is a tuple like (5, 10), and x[0] is 5.

So the sorting compares start times"""

""" (5, 10) → 5  
(0, 30) → 0  
(15, 20) → 15


[(0, 30), (5, 10), (15, 20)]

"""


# for i in range(1, len(n)):
#         prev_start, prev_end = n[i - 1]
#         curr_start, curr_end = n[i]

"""Starts a loop from index 1 up to the last index in the list.

We're using indexes instead of looping over elements directly so we can always look at the current and the previous interval.

So, this line means:

"Start at the second interval (index 1), and for each one, compare it to the one before it."

"""

# prev_start, prev_end = n[i - 1]

"""Looks at the previous interval using index i - 1.

n[i - 1] gives you a tuple like (0, 30), and it unpacks that into:

prev_start = 0

prev_end = 30"""

# curr_start, curr_end = n[i]

"""Looks at the current interval at index i.

Unpacks it the same way into:

curr_start = 5

curr_end = 10

"""
# if curr_start < prev_end:

"""This is the core overlap check.

What it means:
"If the current interval starts before the previous one ends..."

Then the two intervals overlap, which is a scheduling conflict."""