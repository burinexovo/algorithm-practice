# Tips

- 使用 Counter 統計累積數量
    count = Counter(nums)

    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    count = {}
    for num in nums:
        if num in cout:
            count = 0
        else:
            count += 1
    
- dict 記得有 .values 可以用 -> 會轉 List

## 概念補充
Bucket Sort:

    # 建 bucket，index 代表頻率
    bucket = [[] for _ in range(len(nums) + 1)]
    
    # 把數字丟進對應頻率的桶
    for num, freq in counter.items():
        bucket[freq].append(num)

    從右往左取 k 個
    result = []
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result