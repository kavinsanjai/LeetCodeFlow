class Solution(object):
    def toGoatLatin(self, sentence):
        words=sentence.split()
        vowels=set('aeiou')
        for i in range(0,len(words)):
            if words[i][0].lower() in vowels:
                words[i]+='ma'+'a'*(i+1)
            elif words[i][0] not in vowels:
                words[i]=words[i][1:]+words[i][0]+'ma'+'a'*(i+1)
        return ' '.join(words)
        