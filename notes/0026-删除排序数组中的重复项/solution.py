# 26. 删除排序数组中的重复项
# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
# 思路：快慢指针原地去重，slow 维护无重复前缀的末尾，fast 探路遇到新元素就放到 slow+1

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        slow,fast=0,0
        #slow表示现有的ok的元素，fast在前面探路，当遇到一个元素nums[fast]!=nums[slow],那么将其放入到nums[slow+1]这里
        while fast < len(nums):
            if nums[fast]!=nums[slow]:
                slow+=1
                # 维护 nums[0..slow] 无重复
                nums[slow]=nums[fast]

            fast+=1
        # 数组长度为索引 + 1
        return slow+1


if __name__ == "__main__":
    s = Solution()

    nums = [1, 1, 2]
    k = s.removeDuplicates(nums)
    assert k == 2 and nums[:k] == [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = s.removeDuplicates(nums)
    assert k == 5 and nums[:k] == [0, 1, 2, 3, 4]

    nums = []
    assert s.removeDuplicates(nums) == 0

    nums = [7]
    k = s.removeDuplicates(nums)
    assert k == 1 and nums[:k] == [7]

    print("all tests passed")
