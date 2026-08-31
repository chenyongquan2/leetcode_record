# 27. 移除元素
# https://leetcode.cn/problems/remove-element/
# 思路：快慢指针，fast 探路，遇到 != val 的元素就压到 nums[slow]，返回 slow 即新长度

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0
        #slow位置为符合要求的元素
        fast,slow=0,0
        while fast<len(nums):
            if nums[fast]!=val:
                #Todo 易错:nums[slow]=val
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow


if __name__ == "__main__":
    s = Solution()

    nums = [3, 2, 2, 3]
    k = s.removeElement(nums, 3)
    assert k == 2 and sorted(nums[:k]) == [2, 2]

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = s.removeElement(nums, 2)
    assert k == 5 and sorted(nums[:k]) == [0, 0, 1, 3, 4]

    nums = []
    assert s.removeElement(nums, 1) == 0

    nums = [7, 7, 7]
    assert s.removeElement(nums, 7) == 0

    print("all tests passed")
