class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new=[]
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if nums1[i]==nums2[j]:
                    new.append(nums1[i])
                    nums1[i]=-1
                    nums2[j]=-1
                    break
        return new