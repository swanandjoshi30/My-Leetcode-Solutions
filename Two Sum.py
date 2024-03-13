class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Get the length of the input list nums
        n = len(nums)
        
        # Iterate through each element in nums
        for i in range(n):
            # Iterate through each element starting from i+1 to the end of nums
            for j in range(i + 1, n):
                # Check if the sum of the current pair of elements equals the target
                if nums[i] + nums[j] == target:
                    # If the sum is equal to the target, return the indices of the pair
                    return [i, j]
        
        # If no such pair is found, return an empty list
        return []
