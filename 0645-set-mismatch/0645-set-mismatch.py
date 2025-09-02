class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        num_set = set()
        duplicate = -1

        for num in nums:
            if num in num_set:
                duplicate = num
            num_set.add(num)

        missing = (n * (n + 1)) // 2 - sum(num_set)
        return [duplicate, missing]


        