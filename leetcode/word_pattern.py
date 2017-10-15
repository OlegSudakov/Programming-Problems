# https://leetcode.com/problems/word-pattern/

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        word2code = {}
        code2word = {}
        words = str.split()
        if len(pattern) != len(words):
            return False
        
        else:
            for i in range(len(pattern)):
                if words[i] not in word2code and pattern[i] not in code2word:
                    word2code[words[i]] = pattern[i]
                    code2word[pattern[i]] = words[i]
                elif words[i] in word2code and pattern[i] in code2word:
                    if word2code[words[i]] != pattern[i] or code2word[pattern[i]] != words[i]:
                        return False
                else:
                    return False
        return True
