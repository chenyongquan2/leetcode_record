# 283. 移动零
# https://leetcode.cn/problems/move-zeroes/
# 思路：快慢指针，先把非零元素依次压到前面（同 27 题移除元素），再把 slow 之后的位置全部补 0

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0:
            return
        fast=slow=0
        while fast<len(nums):
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        #把剩余元素改为0
        while slow<len(nums):
            nums[slow]=0
            slow+=1


if __name__ == "__main__":
    s = Solution()

    nums = [0, 1, 0, 3, 12]
    s.moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

    nums = [0]
    s.moveZeroes(nums)
    assert nums == [0]

    nums = [1, 2, 3]
    s.moveZeroes(nums)
    assert nums == [1, 2, 3]

    nums = [0, 0, 1]
    s.moveZeroes(nums)
    assert nums == [1, 0, 0]

    print("all tests passed")
