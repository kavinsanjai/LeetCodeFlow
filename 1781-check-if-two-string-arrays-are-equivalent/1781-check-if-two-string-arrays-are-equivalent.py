class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        return True if ''.join(word1) == ''.join(word2) else False
        