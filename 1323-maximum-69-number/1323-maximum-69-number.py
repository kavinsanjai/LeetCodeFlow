class Solution(object):
    def maximum69Number (self, num):
        num=str(num)
        i=num.find('6')
        if i==-1:
            return int(num)
        return int(num[:i]+'9'+num[i+1:])
        