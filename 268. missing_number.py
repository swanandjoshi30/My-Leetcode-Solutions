class Solution:
    def missingNumber(self, nums):
        # Get the length of the input list 'nums'
        n = len(nums)

        # Calculate the sum of the first 'n' natural numbers using the formula n*(n+1)/2
        total = n * (n + 1) // 2

        # Calculate the sum of the elements in the given list 'nums'
        sum_res = sum(nums)

        # The missing number is the difference between the total sum and the sum of the list
        total_ans = total - sum_res

        # Return the missing number
        return total_ans