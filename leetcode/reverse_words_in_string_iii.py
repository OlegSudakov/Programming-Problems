# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([word[::-1] for word in s.split()])
