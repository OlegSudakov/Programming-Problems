# https://leetcode.com/problems/judge-route-circle/

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        move_dict = {"U": (0, +1), "D": (0, -1), "L": (-1, 0), "R":(+1, 0)}
        x, y = 0, 0
        for move in moves:
            if move in move_dict:
                x += move_dict[move][0]
                y += move_dict[move][1]
        if x==0 and y==0:
            return True
        else:
            return False
