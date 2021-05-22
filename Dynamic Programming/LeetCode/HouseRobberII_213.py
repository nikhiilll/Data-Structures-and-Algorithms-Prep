def rob(nums):

    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    def robHelper(array):

        robbery = [0 for _ in range(len(array) + 1)]
        robbery[1] = array[0]

        for i in range(2, len(array) + 1):
            robbery[i] = max(robbery[i - 1], robbery[i - 2] + array[i - 1])

        return robbery[-1]

    return max(robHelper(nums[:-1]), robHelper(nums[1:]))
