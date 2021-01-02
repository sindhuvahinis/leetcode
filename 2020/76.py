class Solution:
    def nextCells(self, cells, n):
        newcells = [0] * n

        for i in range(1, n - 1):
            if cells[i - 1] == cells[i + 1]:
                newcells[i] = 1
            else:
                newcells[i] = 0

        return newcells

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        n = len(cells)

        i = 0
        is_repeated_found = False
        visited = set()

        while N > 0:

            if not is_repeated_found:
                curr_state = tuple(self.nextCells(cells, n))

                if curr_state in visited:
                    is_repeated_found = True
                    N = N % i
                else:
                    visited.add(curr_state)
                    i += 1

            if N > 0:
                cells = self.nextCells(cells, n)
                N -= 1

        return cells