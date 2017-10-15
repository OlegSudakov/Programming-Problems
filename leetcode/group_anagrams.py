# https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def compute_configuration(self, word, dict):
        conf = [0]*len(dict)
        for char in word:
            conf[dict[char]] += 1
        return conf
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        index = 0
        for string in strs:
            for char in string:
                if char not in dict:
                    dict[char] = index
                    index += 1
        confs = {}
        index = 0
        result = []
        for string in strs:
            conf = tuple(self.compute_configuration(string, dict))
            if conf in confs:
                result[confs[conf]].append(string)
            else:
                confs[conf] = index
                index += 1
                result.append([string])
        return result
