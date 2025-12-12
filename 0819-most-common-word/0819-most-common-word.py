class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph=re.sub('[^\w]',' ',paragraph.lower())
        paragraph=paragraph.split()
        fre=Counter(paragraph)
        fre = sorted(fre.items(), key=lambda x: x[1], reverse=True)
        for i,j in fre:
            if i not in banned:
                return i
        
        