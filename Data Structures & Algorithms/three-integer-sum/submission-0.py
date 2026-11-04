class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        #iterate through nums for number i such that some j and k exist to fullfill -i = j + k
        #j and k are searched with l and r pointers in 2pointer algorithm
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                threeSum = a + nums[j] + nums[k]
                if threeSum > 0: k -= 1
                elif threeSum < 0: j += 1
                else:
                    res.append([a, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res