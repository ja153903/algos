from collections import namedtuple

Car = namedtuple("Car", ["position", "speed"])


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """
        There are n cars going to the same destination along a one-lane road. The destination is target miles away.

        You are given two integer array position and speed, both of length n, where position[i] is the position of the
        ith car and speed[i] is the speed of the ith car (in miles per hour).

        A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed.
        The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored
        (i.e., they are assumed to have the same position).

        A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

        If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

        Return the number of car fleets that will arrive at the destination.

        Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
        Output: 3

        - reverse sort position and speed by position
        - compute y = mx + b as x = (y - b) // m
            - In this case position[i] is b speed[i] is m and target is y
        - iterate over the positions and speeds keeping track of x within a stack
        - if a newly computed x is greater than an existing value on the stack then increment the result and push x to the stack

        This problems runs in O(n log n) time and O(n) space
        """
        if not position or not speed:
            return 0

        stack = []
        result = 1

        data = [Car(position[i], speed[i]) for i in range(len(position))]
        data.sort(key=lambda car: -car.position)

        for b, m in data:
            x = (target - b) / m

            if not stack:
                stack.append(x)
            elif stack[-1] < x:
                result += 1
                stack.append(x)

        return result
