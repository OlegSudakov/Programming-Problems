# https://leetcode.com/problems/friend-circles/

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        total = 0
        visited = set()
        for s in range(len(M)):
            if s not in visited:
                total += 1
                stack = [s]
                while stack:
                    current = stack.pop(0)
                    current_friends = M[current]
                    visited.add(current)
                    for f in range(len(current_friends)):
                        if current_friends[f] == 1 and f != s and f not in visited:
                            stack.append(f)
        return total
