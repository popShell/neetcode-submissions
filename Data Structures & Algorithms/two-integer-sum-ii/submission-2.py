class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            holder = numbers[left] + numbers[right]
            
            if holder > target: right -= 1
            elif holder < target: left += 1
            else: return [left + 1, right +1 ]