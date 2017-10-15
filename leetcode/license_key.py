# https://leetcode.com/problems/license-key-formatting/

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = ""
        count = 0
        for i in range(len(S)-1, -1, -1):
            if S[i] != "-":
                res += S[i].upper()
                count += 1
            if count == K:
                res += "-"
                count = 0
        if len(res) and res[-1] == "-":
            res = res[:-1]
        return res[::-1]
