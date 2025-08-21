class Solution(object):
    def intersection(self, nums1, nums2):
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        new=[]
        for i in range(0,len(nums1)):
            j=0
            while(j<len(nums2)):
                if nums1[i]==nums2[j]:
                    new.append(nums1[i])
                    break
                else:
                    j+=1
        return new