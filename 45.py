
# my initial lengthy solution
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        if not pushed and not popped:
            return True

        if len(pushed) != len(popped):
            return False

        i = j = 0
        n = len(pushed)
        stack = []
        pushedset = set()

        while i < n and j < n:
            if stack and stack[-1] == popped[j]:
                pushedset.add(popped[j])
                stack.pop()
                j += 1
            elif pushed[i] == popped[j]:
                i += 1
                j += 1
            elif popped[j] in pushedset:
                return False
            else:
                stack.append(pushed[i])
                i += 1

        while stack:
            if stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                return False

        return True if not stack and j == n else False

# why not use double loops




