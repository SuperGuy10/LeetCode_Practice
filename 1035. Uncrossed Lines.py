'''
We write the integers of A and B (in the order they are given) on two separate horizontal lines.
Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:
A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.
Return the maximum number of connecting lines we can draw in this way.

Example 1:
1   4   2
|     /
1   2   4 

Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.

Example 2:
Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3

Example 3:
Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2
 

Note:
1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000
'''

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)
        table = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                table[i][j] = max(table[i-1][j-1]+(A[i-1]==B[j-1]),table[i-1][j],table[i][j-1])
        return table[-1][-1]
        
#solution2

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)
        return self.LCS(A,B,m,n)
    def LCS(self, L1, L2, len1, len2):
        table = [[0]*(len2+1) for _ in range(len1+1)]
        #print(table)
        for i in range(len1+1):
            for j in range(len2+1):
                if i == 0 or j == 0:
                    table[i][j] == 0
                elif L1[i-1] == L2[j-1]:
                    table[i][j] = table[i-1][j-1]+1
                    #print(table)
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])
                #print(table)
        return table[len1][len2]
