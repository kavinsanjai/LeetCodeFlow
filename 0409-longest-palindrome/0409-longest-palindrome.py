class Solution(object):
    def longestPalindrome(self, s):
        count=0
        frequency=Counter(s)
        flag=True
        for i,j in frequency.items():
                if j%2==0:
                    count+=j
                elif i==1 and flag==True:
                    count=count+1
                    flag=False
                elif j%2!=0 :
                    if flag==False:
                        count=count+j-1
                    else:
                        count=count+j
                        flag=False
        return count
