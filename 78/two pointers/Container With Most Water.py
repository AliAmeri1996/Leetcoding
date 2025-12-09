'''Container With Most Water'''

'''You are given an integer array heights where heights[i] represents the height of the 
You may choose any two bars to form a container. Return the maximum amount of water a container can store.'''

'''O(n) time, O(1) space.'''
def container(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right]) #“The container can only be as tall as the shorter wall.”
        area = width * current_height
        max_water = max(max_water, area)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

 
print(container([1,7,2,5,4,7,3,6]))

#while left < right:
'''This loop runs as long as the left pointer is to the left of the right pointer. In other words, it continues while there are still at least two bars to form a container.'''

#width = right - left
'''calculates the horizontal distance between the two pointers, which is the width of the container.'''

#current_height = min(height[left], height[right])
'''s determining the height of the water container, based on the shorter of the two bars at the left and right pointers.'''

#if height[left] < height[right]:
            #left += 1
        #else:
            #right -= 1
'''The height of the container is limited by the shorter bar.

So if you want a chance to increase the area, you need to possibly find a taller bar.

Moving the taller bar doesn’t help — the shorter one is still limiting the height.

By moving the shorter bar, you open up the possibility of finding a taller bar on that side, and (even though width shrinks), if height increases enough, the overall area might improve.'''