class NumArray(object):

    def __init__(self, nums):
        self.prefix=[]
        curr=0
        for i in range(0,len(nums)):
            curr+=nums[i]
            self.prefix.append(curr)
    def sumRange(self, left, right):
        rightsum=self.prefix[right]
        leftsum=self.prefix[left-1] if left>0 else 0
        return rightsum-leftsum



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)