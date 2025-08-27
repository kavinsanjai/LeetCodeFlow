class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        revised=re.sub(r'[0-9 ]',"",licensePlate.lower())
        frequency=Counter(revised)
        result=None
        for i in range(0,len(words)):
            word_count = Counter(words[i].lower())
            if all(word_count[ch] >= frequency[ch] for ch in frequency):
                    if result is None or len(words[i])<len(result):
                        result=words[i]
        return result
        