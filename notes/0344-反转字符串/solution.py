# 344. 反转字符串
# https://leetcode.cn/problems/reverse-string/
# 思路：首尾双指针，向中间靠拢，逐对交换。

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #双指针
        lo,hi=0,len(s)-1
        while lo<hi:
            tmp=s[lo]
            s[lo]=s[hi]
            s[hi]=tmp
            lo+=1
            hi-=1


if __name__ == "__main__":
    sol = Solution()

    s1 = ["h", "e", "l", "l", "o"]
    sol.reverseString(s1)
    assert s1 == ["o", "l", "l", "e", "h"]

    s2 = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(s2)
    assert s2 == ["h", "a", "n", "n", "a", "H"]

    s3 = ["a"]
    sol.reverseString(s3)
    assert s3 == ["a"]

    print("all tests passed")
