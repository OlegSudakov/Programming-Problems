# https://leetcode.com/problems/replace-words/

import re

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dict = set(dict)
        def replace(word):
            for i in range(len(word)):
                if word[:i] in dict:
                    return word[:i]
            return word
        return " ".join(map(replace, sentence.split()))
