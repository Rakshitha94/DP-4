# Leetcode:accepted
# bruteforce
# tc: (m*N)3
# sc:o(1)
# youtake a sliding window diagonally downwards from the grid that is 1 and check the rows (towords left) and cols(towards up) to check if they are all ones.IF they are all ones, you increase the curr and again go the next diagonal place


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        if rows == 0:
            return 0
        cols = len(matrix[0])
        max1 = 0
        flag = False
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    flag = True
                    curr = 1
                    while (i + curr < rows and j + curr < cols and flag):
                        for k in range(i + curr, i - 1, -1):
                            if matrix[k][j + curr] == '0':
                                flag = False
                                break

                        for k in range(j + curr, j - 1, -1):
                            if matrix[i + curr][k] == '0':
                                flag = False
                                break
                        if flag:
                            curr += 1
                    max1 = max(max1, curr)
        return max1 ** 2


# leetcode:accepted
# tc: o(MN)
# sc:o(MN)
# no doubts
# explianation:  make a dp matrix of one more size and if the matrix has value of 1, then go to the subsequent dp matrix and check the three side(left, top left and top) amd find the minimum and add 1 to it and keep feeling the dp array like this in accordnce to the matrix


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        if rows == 0:
            return 0
        max1 = 0
        cols = len(matrix[0])
        dp = [[0 for i in range(cols + 1)] for j in range(rows + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

                max1 = max(max1, dp[i][j])
        return max1 ** 2



