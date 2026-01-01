class Solution(object):
    def plusOne(self, digits):
        num=''
        for i in digits:
            num=num+str(i)
        num_plus=str(int(num)+1)
        return [int(i) for i in num_plus]        
        
            
