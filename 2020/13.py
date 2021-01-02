class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def recur(board, word, row, col, index):

            if index == len(word):
                return True

            elif index > len(word) or row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][
                col] == '0' or word[index] != board[row][col]:
                return False

            index += 1

            prev, board[row][col] = board[row][col], '0'

            rValue = recur(board, word, row + 1, col, index) or recur(board, word, (row - 1), col, index) or recur(
                board, word, row, col + 1, index) or recur(board, word, row, col - 1, index)

            board[row][col] = prev

            return rValue

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (recur(board, word, i, j, 0)):
                    return True

        return False