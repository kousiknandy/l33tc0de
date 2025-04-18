class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, left, right, pindex):
            pivot = nums[pindex]
            nums[pindex], nums[right] = nums[right], nums[pindex]
            part = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[part], nums[i] = nums[i], nums[part]
                    part += 1
            nums[part], nums[right] = nums[right], nums[part]
            return part

        def select(nums, left, right, k):
            while True:
                if left == right: return nums[left]
                pindex = right # (left + right) // 2
                pindex = partition(nums, left, right, pindex)
                # print(pindex,left, right, nums)
                if k == pindex: return nums[k]
                if k < pindex: right = pindex - 1
                else: left = pindex + 1

        return select(nums, 0, len(nums)-1, len(nums)-k)
