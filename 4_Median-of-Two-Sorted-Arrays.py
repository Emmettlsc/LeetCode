class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Merge lists
        temp = nums1 + nums2
        #sort 
        temp.sort()
        if len(temp)%2 == 0:
            return (temp[int(len(temp)/2)] + temp[int(len(temp)/2-1)])/2.0
        return float(temp[int(len(temp)/2)])
