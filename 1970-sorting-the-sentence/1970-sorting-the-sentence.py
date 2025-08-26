class Solution(object):
    def sortSentence(self, s):
        words=s.split()
        new_words=sorted(words,key=lambda x:int(x[-1]))
        return  ' '.join(w[:-1] for w in new_words) 
      