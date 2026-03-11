'''
# 核心概念：
• 每一輪做一件事：從「未排序區域」找最小值 → 放到最前面
• 換句話說：每一輪都會讓 已排序區域 +1(左邊：已排序 右邊：未排序)
'''

# nums = [64, 25, 12, 22, 11]

# 每次從 i 開始往後找最最小的，跟 i 交換
def selection_sort(nums):
    n = len(nums)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j

        nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums


print(selection_sort([64, 25, 12, 22, 11]))
# [11, 12, 22, 25, 64]
