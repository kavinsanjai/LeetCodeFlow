class Solution(object):
    def truncateSentence(self, s, k):
        word_list=s.split()
        return ' '.join(word_list[:k])
        