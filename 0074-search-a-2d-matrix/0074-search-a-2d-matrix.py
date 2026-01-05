class Solution(object):
    def searchMatrix(self, matrix, target):
        # nums=[]
        # for i in range(0,len(matrix)):
        #     nums+=matrix[i]
        
        # start=0
        # end=len(nums)-1
        # while(start<=end):
        #     mid=start+(end-start)//2
        #     if nums[mid]==target:
        #         return True
        #     elif nums[mid]>target:
        #         end=mid-1
        #     else:
        #         start=mid+1
        # return False
        for i in range(0,len(matrix)):
            if matrix[i][0]<=target and matrix[i][len(matrix[i])-1]>=target:
                start=0
                end=len(matrix[i])-1
                while(start<=end):
                    mid=start+(end-start)//2
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]>target:
                        end=mid-1
                    else:
                        start=mid+1
        return False
                    