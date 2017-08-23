class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 > l2:
            return self.findMedianSortedArrays(nums2, nums1)
        imin = 0
        imax = l1
        mid = (l1 + l2 + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = mid - i
            if i < l1 and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[i-1]
                else:
                    max_left = max(nums1[i-1], nums2[j-1])
                if (l1 + l2) % 2 == 1:
                    return max_left
                if i == l1:
                    min_right = nums2[j]
                elif j == l2:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])
                return (max_left + min_right) / float(2)
            
#         if nums1 == [] or nums2 == [] or nums1[0] > nums2[-1]:
#             return self.median(nums2+nums1)
#         if nums2[0] > nums1[-1]:
#             return self.median(nums1+nums2)
#         i = 0
#         j = 0
#         nums = []
#         while i != len(nums1) and j != len(nums2):
#             if nums1[i] < nums2[j]:
#                 nums.append(nums1[i])
#                 i += 1
#             else:
#                 nums.append(nums2[j])
#                 j += 1
#         if i != nums1:
#             nums += nums1[i:]
#         if j != nums2:
#             nums += nums2[j:]
#         return self.median(nums)
    
#     def median(self, nums):
#         mid = len(nums)//2
#         if len(nums) % 2 == 0:
#             return (nums[mid-1]+nums[mid])/ float(2)
#         return nums[mid]
