class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack=[]
        nge=[-1]*len(nums2)
        for i in range(len(nums2)):
            while stack and nums2[i]>nums2[stack[-1]]:
                index=stack.pop()
                nge[index]=nums2[i] 
            stack.append(i)

        new={}
        for i in range(0,len(nge)):
            new[nums2[i]]=nge[i]
        

        for i in range(0,len(nums1)):
            nums1[i]=new[nums1[i]]
            
        return nums1