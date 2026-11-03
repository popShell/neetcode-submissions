class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index = {}

        for i, n in enumerate(numbers, start=1):
            index[n] = i

        for i, n in enumerate(numbers, start=1):
            diff = target - n
            if diff in index and index[diff] != i:
                return [i, index[diff]]
        return []