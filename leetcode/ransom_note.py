# https://leetcode.com/problems/ransom-note/

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = {}
        for letter in magazine:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
        
        for letter in ransomNote:
            if letter in counts:
                if counts[letter] == 0:
                    return False
                else:
                    counts[letter] -= 1
            else:
                return False
        return True
