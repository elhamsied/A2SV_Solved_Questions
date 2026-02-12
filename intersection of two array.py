class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cha = set(nums1)
        cha2 = set(nums2)
        com = list(cha & cha2)
        return com
