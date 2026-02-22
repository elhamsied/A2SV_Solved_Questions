class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        map_ = {}
        for i,rest in enumerate(list1):
            map_[rest] = i
        mini = float('inf')
        res = []
        for j,rest in enumerate(list2):
            if rest in map_:
                current_sum = map_[rest] + j
                if current_sum < mini:
                    mini = current_sum
                    res = [rest]
                elif current_sum == mini:
                    res.append(rest)
        return res
 
 
   
