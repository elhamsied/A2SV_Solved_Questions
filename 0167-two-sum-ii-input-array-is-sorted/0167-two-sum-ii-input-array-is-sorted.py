class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        vl=0
        pt = len(numbers)-1
        while pt<len(numbers):
            if numbers[vl] +numbers[pt] == target:
                return [vl + 1,pt +1]
            elif numbers[vl] +numbers[pt] < target:
                vl+=1
            else:
                pt-=1
