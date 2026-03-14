class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans =[]
        my_dict = {}
        for i in nums2:
            while ans and i >ans[-1]:
                prev = ans.pop()
                my_dict[prev] = i
            
            ans.append(i)

        result = []

        for num in nums1:
            result.append(my_dict.get(num, -1))

        return result