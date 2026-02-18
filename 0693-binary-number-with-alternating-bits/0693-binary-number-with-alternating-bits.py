class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary=str(format(n,'b'))
        for i in range(1,len(binary)):
            if binary[i-1]==binary[i]:
                return False
        else:
            return True