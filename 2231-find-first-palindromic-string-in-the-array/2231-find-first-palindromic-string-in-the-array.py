class Solution(object):
    def firstPalindrome(self, words):
        for i in range(0,len(words)):
            if words[i][::-1]==words[i]:
                return words[i]
        return ""