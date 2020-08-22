class Solution:
    def generateParenthesis(self, n: int):

        def recur(plist, n: int, currStr, nopen=0, nclose=0):
            if nclose == n:
                plist.append(currStr)
                return

            if nopen > nclose:
                recur(plist, n, currStr + ")", nopen, nclose + 1)

            if nopen < n:
                recur(plist, n, currStr + "(", nopen + 1, nclose)

        res = []
        recur(res, int(n), "")
        return res