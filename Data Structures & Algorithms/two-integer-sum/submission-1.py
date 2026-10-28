class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        #load all values of nums into hash
        for i, n in enumerate(nums):
            index[n] = i

        #iterate through nums finding diff for each value at index i
        #check if diff value exists in hash if so check if same index as value n
        #if no return value 
        for i, n in enumerate(nums):
            diff = target - n
            if diff in index and index[diff] != i:
                return [i, index[diff]]
        return []