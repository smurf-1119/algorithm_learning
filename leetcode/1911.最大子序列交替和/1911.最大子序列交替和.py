def maxAlternatingSum(nums) -> int:
    # even表示序列最后一个数字为偶数下标(长度为奇数)
    # odd表示序列最后一个数字为奇数下标(长度为偶数)
    even, odd = nums[0], 0
    for i in range(1, len(nums)):
        even, odd = max(even, odd + nums[i]), max(odd, even - nums[i])
    # 从递推公式发现even>odd
    return even

print(maxAlternatingSum([4,2,5,3]))