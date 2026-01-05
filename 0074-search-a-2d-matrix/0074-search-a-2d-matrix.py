class Solution(object):
    def searchMatrix(self, matrix, target):
        nums=[]
        for i in range(0,len(matrix)):
            nums+=matrix[i]
        
        start=0
        end=len(nums)-1
        while(start<=end):
            mid=start+(end-start)//2
            if nums[mid]==target:
                return True
            elif nums[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return False
            