#1306. Jump Game III
#https://leetcode.com/problems/jump-game-iii/description/?envType=daily-question&envId=2026-05-17
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        return self.canReachRecurse(arr,start, set(), False)

    def canReachRecurse(self, arr: List[int], start: int, searched: set, result: bool) -> bool:
        searched.add(start)
        if arr[start] == 0:
            return True
        else:
            newStartPlus = start + arr[start]
            if (newStartPlus < len(arr) and newStartPlus >= 0) and newStartPlus not in searched:
                result = self.canReachRecurse(arr = arr, start = newStartPlus, searched = searched, result = False)
            newStartMinus = start - arr[start]
            if (newStartMinus < len(arr) and newStartMinus >= 0) and newStartMinus not in searched and result == False:
                result = self.canReachRecurse(arr = arr, start = newStartMinus, searched = searched, result  = False)
        return result
        