class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        mini=float('inf')
        min_i=float('inf')
        letter=''
        for i in range(0,len(letters)):
            if ord(letters[i])>ord(target):
                mini=ord(letters[i])
                if min_i>mini:
                    min_i=mini
                    letter=letters[i]
        return letter if letter!='' else letters[0]