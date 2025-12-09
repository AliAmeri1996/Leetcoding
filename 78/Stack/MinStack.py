'''Design a stack class that supports the push, pop, top, and getMin operations.'''


class MinStack:
    def __init__(self):
        self.stack = []      # holds values
        self.min_stack = []  # holds current mins (same length as stack)

    def push(self, val: int) -> None:
        if not self.min_stack:
           self.min_stack.append(val)# since we're pushing the first element, so its automatically the mis
        else:
           current_min = self.min_stack[-1]
           if val < current_min:
              self.min_stack.append(val)
           else:
              self.min_stack.append(current_min)

    # Always push the actual value to the main stack
        self.stack.append(val)

        '''So every time you call push(val) on your MinStack, the value goes into two places:
           self.stack → to keep the real data.
           self.min_stack → to track the current minimum.'''

    def pop(self) -> None:
        # Assumes pop is called only when non-empty
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


#if not self.min_stack:
'''it means if the stack is empty'''
#min_stack[-1] 
'''in stack basically this measn the last element pushed to the list'''


# else:
#            current_min = self.min_stack[-1]
#            if val < current_min:
#               self.min_stack.append(val)
#            else:
#               self.min_stack.append(current_min)
'''The top of min_stack always stores the minimum value so far.

When a new value val is pushed:

If val < current_min → this new value is the new minimum → push val onto min_stack.

Else → the old minimum is still smaller → push current_min again onto min_stack'''


ms = MinStack()

ms.push(5)      # stack=[5], min_stack=[5]
ms.push(3)      # stack=[5,3], min_stack=[5,3]
ms.push(7)      # stack=[5,3,7], min_stack=[5,3,3]

print(ms.top())     # -> 7   (last pushed element)
print(ms.getMin())  # -> 3   (minimum so far)

ms.pop()        # removes 7
# stack=[5,3], min_stack=[5,3]

print(ms.top())     # -> 3
print(ms.getMin())  # -> 3

ms.pop()        # removes 3
# stack=[5], min_stack=[5]

print(ms.top())     # -> 5
print(ms.getMin())  # -> 5