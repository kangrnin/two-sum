from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    idx1, idx2 = 0, 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                idx1, idx2 = i, j
                break
    return [idx1, idx2]
