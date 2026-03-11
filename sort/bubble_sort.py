'''
# 核心概念：
每一輪都去比較相鄰兩個元素：
• 如果前面比後面大，就交換
• 一輪結束後，最大值會被推到最右邊
'''

# nums = [5, 3, 8, 4]


# 會多跑
# •	第一輪結束，最後一個已經排好了
# •	第二輪結束，倒數第二個也排好了
# •	所以後面不用一直比到最後
def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        for j in range(n - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

# 每次跑完 - i 已經排好的最大值不需要再比
def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        for j in range(0, n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


print(bubble_sort([5, 3, 8, 4]))
# [3, 4, 5, 8]
