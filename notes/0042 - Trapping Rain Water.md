思路：目前位置 i 左邊最大與右邊最大的柱子取最小 - height[i] (當下水位)
min(leftMax, rightMax) - height[i] -> 代表當下 i 可填的水量 (-height[i] 扣除腳底下的方塊)

height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
leftMax = [0, 2, 2, 3, 3, 3, 3, 3, 3, 3]
rightMax = [3, 3, 3, 3, 3, 3, 3, 3, 2, 1]
