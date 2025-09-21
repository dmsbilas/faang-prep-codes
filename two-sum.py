# https://leetcode.com/problems/two-sum/description/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# This is O(n^2) time complexity and O(1) space complexity.
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))


# This is O(n) time complexity and O(n) space complexity.
def two_sum_hashmap(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        if target - nums[i] in hashmap:
            return [hashmap[target - nums[i]], i]
        hashmap[nums[i]] = i
    return []

print(two_sum_hashmap([2, 7, 11, 15], 9))
print(two_sum_hashmap([3, 2, 4], 6))
print(two_sum_hashmap([3, 3], 6))