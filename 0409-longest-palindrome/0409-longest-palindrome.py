class Solution(object):
    def longestPalindrome(self, s):
        fre=Counter(s).most_common()
        count=0
        seen=False
        for i,j in fre:
            if j%2==0:
                count+=j
            else:
                if seen:
                    count+=j-1
                else:
                    seen=True
                    count+=j
        return count
            

        
        