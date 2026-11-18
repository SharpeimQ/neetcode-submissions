class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiplication is associative
        # calculte left and right running product
        # combine

        left = []
        length = len(nums)
        right = [1] * length

        product = 1
        for i in range(length):
            if i == 0:
                left.append(1)
                continue
            
            product *= nums[i - 1]
            left.append(product)

        product = 1
        for i in range(length - 1, -1, -1):
            if i == length - 1:
                right[i] = 1
                continue
            
            product *= nums[i + 1]
            right[i] = product

        result = []
        for i in range(length):
            result.append(left[i] * right[i])

        return result            

                
