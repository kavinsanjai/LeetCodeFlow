class Solution:
    def subtractProductAndSum(self, n: int) -> int:
            value=str(n)
            sum1=0
            pro1=1
            for i in range(0,len(value)):
                digit=int(value[i])
                sum1+=digit
                pro1*=digit
            return pro1-sum1