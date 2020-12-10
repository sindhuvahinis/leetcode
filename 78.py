from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        queue.append((beginWord, 1))

        wordList = set(wordList)

        while queue:
            word, count = queue.popleft()

            if word == endWord:
                return count

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newword = word[:i] + c + word[i + 1:]
                    if newword in wordList:
                        wordList.remove(newword)
                        queue.append((newword, count + 1))

        return 0