'''Car Fleet'''
def carFleet(target, position, speed) -> int:
    cars = sorted(zip(position, speed), reverse=True)  # sort by position desc
    fleets = 0
    slowest_time = 0.0

    for p, s in cars:
        t = (target - p) / s
        if t > slowest_time:
            fleets += 1
            slowest_time = t
        # else: merges with the fleet ahead

    return fleets

       






print(carFleet(target=10,position=[4,1,0,7],speed=[2,2,1,1]
))


#zip creates pairs
'''position=[1,4]
   speed=[3,2]
   
with zip it would be [(1, 3), (4, 2)]'''

#sorted(zip(position, speed), reverse=True)
'''it sorted the numbers of the first tuple
[(4, 2), (1, 2), (0, 1), (7, 1)] this is the zip
[(4, 2), (1, 2), (0, 1), (7, 1)] this is the sorted


'''
