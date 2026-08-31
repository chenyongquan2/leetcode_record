# 167. 两数之和 II - 输入有序数组
# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
# 思路：数组已升序，左右双指针相向收缩，和偏大移右指针、偏小移左指针

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo,hi=0,len(numbers)-1
        while lo<hi:
            sum=numbers[lo]+numbers[hi]
            if sum==target:
                return [lo+1,hi+1]
            elif sum>target:
                hi-=1
            else:
                lo+=1
        return [-1,-1]


if __name__ == "__main__":
    s = Solution()

    assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert s.twoSum([2, 3, 4], 6) == [1, 3]
    assert s.twoSum([-1, 0], -1) == [1, 2]

    print("all tests passed")
