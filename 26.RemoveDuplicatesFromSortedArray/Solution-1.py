class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueNums = []
        counts = 0
        for num in nums:
            if num not in uniqueNums:
                uniqueNums.append(num)
                counts += 1
        
        nums[:] = uniqueNums
        return counts
        