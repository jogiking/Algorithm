class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, mid, right = [], [], []
        for element in nums:
            if element<pivot:
                left.append(element)
            elif element==pivot:
                mid.append(element)
            else:
                right.append(element)
        return left+mid+right
