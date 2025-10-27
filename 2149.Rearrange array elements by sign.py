class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * n

        posIndex = 0
        negIndex = 1

        for num in nums:
            if num > 0:
                arr[posIndex] = num
                posIndex += 2
            else:
                arr[negIndex] = num
                negIndex += 2
        return arr
