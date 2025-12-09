def dailyTemperatures(temperatures):
        n = len(temperatures)
        res = [0] * n   # creates a list of length n filled with zeros.
        stack = []      # holds indices

        for i in range(n):
            # Check if current temp is warmer than the day on top of stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = i - prev_day
            stack.append(i)

        return res

print(dailyTemperatures([30,38,30,36,35,40,28]
))
# output:[1, 4, 1, 2, 1, 0, 0]

#res = [0] * n
'''creates a list of length n where every element is 0.
if length n=7 res=[0, 0, 0, 0, 0, 0, 0]'''

#while stack 
'''only continue ehile stack is not empty'''

#temperatures[stack[-1]]
'''“look up the temperature at the index that’s on top of the stack.”'''