"""
@Title: 260. Single Number III
@Tag: 
@Date: Feb-20 2020
@Author: ceezyyy
@Difficulty: Medium
"""


import collections


# Solution one(sort & one pass)


class Solution:
    def singleNumber(self, N: List[int]) -> List[int]:
        N, n, res = sorted(N), len(N), []
        if N[0] != N[1]:  # front
            res.append(N[0])
        if N[-1] != N[-2]:  # back
            res.append(N[-1])
        for i in range(1, n-1):  # mid
            if N[i] != N[i-1] and N[i] != N[i+1]:
                res.append(N[i])
        return res


"""
Runtime: 56 ms, faster than 89.05% of Python3 online submissions for Single Number III.
Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Single Number III.
"""


"""
Time Complexity: O(nlogn)
Space Complexity: O(1)
"""


# Solution two(hashmap & two pass)


class Solution:
    def singleNumber(self, N: List[int]) -> List[int]:
        res, d = [], collections.defaultdict(int)
        for n in N:
            d[n] += 1
        for n in N:
            if d[n] == 1:
                res.append(n)
        return res


"""
Runtime: 60 ms, faster than 72.33% of Python3 online submissions for Single Number III.
Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Single Number III.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
