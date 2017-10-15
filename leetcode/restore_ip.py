# https://leetcode.com/problems/restore-ip-addresses/

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self.__restoreIpAddresses(s, "", 0)
        return self.res
    
    def __restoreIpAddresses(self, s, buffer, num_count):
        if not s and num_count < 4:
            return
        if num_count == 4:
            if not s:
                self.res.append(buffer)
            return
        num = s[:1]
        if num_count > 0:
            buffer += "."
        self.__restoreIpAddresses(s[1:], buffer + num, num_count + 1)
        if len(s) > 1:
            num = s[:2]
            if num[0] == "0" or int(num) > 255:
                return
            self.__restoreIpAddresses(s[2:], buffer + num, num_count + 1)
        if len(s) > 2:
            num = s[:3]
            if num[0] == "0" or int(num) > 255:
                return
            self.__restoreIpAddresses(s[3:], buffer + num, num_count + 1)
