# https://leetcode.com/problems/detect-capital/

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.lower()[1:] == word[1:]:
            return True
        if word.upper() == word:
            return True
        return False
