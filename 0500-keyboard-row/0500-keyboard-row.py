class Solution(object):
    def findWords(self, words):
        result=[]
        row1=set("qwertyuiop")
        row2=set("asdfghjkl")
        row3=set("zxcvbnm")

        for i in range(0,len(words)):
            lower_word=set(words[i].lower())
            if lower_word <= row1 or lower_word <= row2 or lower_word <= row3:
                result.append(words[i])
        return result
                    