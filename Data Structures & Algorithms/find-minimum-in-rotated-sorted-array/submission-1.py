class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            if l == r:
                return nums[l]
            mid = l + (r-l)//2
            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
            elif nums[mid+1] > nums[mid] and nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[mid+1] > nums[mid] and nums[r] < nums[mid]:
                l = mid+1
            elif nums[mid+1] > nums[mid] and nums[r] > nums[mid]:
                r = mid-1
        
        return nums[l]