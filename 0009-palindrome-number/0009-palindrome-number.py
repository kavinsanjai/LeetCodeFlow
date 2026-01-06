class Solution(object):
    def isPalindrome(self, x):
        # num=0
        # key=x
        # while(key>0):
        #     rem=key%10
        #     num = num*10 + rem
        #     print(num)
        #     key=key//10
        # if(num==x):
        #     return True
        # else:
        #     return False
        
        


        # if(x>=0):
        #     reverse=int(str(x)[::-1])
        #     if (reverse==x):
        #         return True
        #     else:
        #         return False 
        # return False           

        x=str(x)
        left=0
        right=len(x)-1
        while(left<right):
            if x[left]==x[right]:
                left+=1
                right-=1
            else:
                return False
        return True