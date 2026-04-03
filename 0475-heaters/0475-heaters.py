class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        k = 0
        max_rad = 0
        for i in houses:
            while k < len(heaters) - 1 and abs(heaters[k+1] - i) <= abs(heaters[k] - i):
                k += 1
            dis = abs(heaters[k] - i)

            max_rad = max(max_rad, dis)
        return max_rad
