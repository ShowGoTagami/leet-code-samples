class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        list = []
        for num in range(0, len(nums), 2):
            for i in range(nums[num]):
                list.append(nums[num+1])
        return list
