class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for num in nums:

            index1 = nums.index(num)
            for x in nums[index1+1:]:
                if target == num + x:

                    if nums.index(x) != nums.index(num):
                        index2 = nums.index(x)
                    elif num == x:
                        index2 = nums.index(x, (index1+1))

                    solution = [index1, index2]
                    return solution
