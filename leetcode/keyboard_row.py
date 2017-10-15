# https://leetcode.com/problems/keyboard-row/

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_1 = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
        row_2 = {"a", "s", "d", "f", "g", "h", "j", "k", "l"}
        row_3 = {"z", "x", "c", "v", "b", "n", "m"}
        result = []
        for word in words:
            new_word = word.lower()
            first_char = new_word[0]
            add_flag = True
            if first_char in row_1:
                for char in new_word:
                    if char not in row_1:
                        add_flag = False
                        break
            elif first_char in row_2:
                for char in new_word:
                    if char not in row_2:
                        add_flag = False
                        break
            elif first_char in row_3:
                for char in new_word:
                    if char not in row_3:
                        add_flag = False
                        break
            if add_flag:
                result.append(word)
        return result
                    
