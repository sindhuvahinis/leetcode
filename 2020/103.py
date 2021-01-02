class Solution:

    def willMeet(self, asteroid1, asteroid2):
        return (asteroid1 > 0 and asteroid2 < 0)

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        # iterate through each asteroid
        # if the previous asteriod and current is in different direction, then explode the small one
        # continue with this till the previous one
        # return the result stack

        for asteroid in asteroids:

            curr = asteroid

            while stack and self.willMeet(stack[-1], curr):
                prev = stack.pop()

                if abs(prev) > abs(curr):
                    curr = prev
                elif abs(prev) == abs(curr):
                    curr = 0

            if curr:
                stack.append(curr)

        return stack