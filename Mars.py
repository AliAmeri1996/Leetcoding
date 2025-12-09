import sys
import math



distance = int(input())
time = int(input())
velocity = int(input())
fuel = int(input())
fuel_consumption = int(input())
if velocity * time < distance:
    print('Failure, Not enough time')
elif fuel * fuel_consumption < distance:
    print('Failure, Not enough fuel')
else:
    print('Welcome to Mars')