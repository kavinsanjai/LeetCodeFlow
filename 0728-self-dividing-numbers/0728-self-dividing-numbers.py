class Solution(object):
    def selfDividingNumbers(self, left, right):
        output = []
        for i in range(left, right + 1):
            is_self_dividing = True
            for digit in str(i):
                if digit == "0" or i % int(digit) != 0:
                    is_self_dividing = False
                    break
            if is_self_dividing:
                output.append(i)
        return output
