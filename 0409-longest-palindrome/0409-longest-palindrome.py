class Solution(object):
    def longestPalindrome(self, s):
        fre=Counter(s)
        maxi=0
        count=0
        for i,j in fre.items():
            if j%2==0:
                count+=j
            elif j%2!=0:
                if j>maxi:
                    if maxi>0:
                        count+=maxi-1
                    maxi=j
                else:
                    rem=j-1
                    count+=rem
        count+=maxi
        return count
            

        
        