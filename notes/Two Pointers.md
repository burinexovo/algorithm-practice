# Tips

- A-Za-z0-9

  ```python
  # 方法一：用正規表達式
  import re

  s = "Hello@123!!世界"
  result = re.sub(r'[^A-Za-z0-9]', '', s)

  print(result) # Hello123
  ```

  ```python
  # 方法二：用字元判斷
  s = "Hello@123!!世界"

  result = ''.join(c for c in s if c.isalnum() and c.isascii())

  print(result)   # Hello123
  ```

  ```python
  # 方法二：用字元判斷
  s = "Hello@123!!世界"

  # 加 isascii() 主要是因為 c.isalnum() 遇到中文也會是 True
  result = ''.join(c for c in s if c.isalnum() and c.isascii())

  print(result)   # Hello123
  ```

  ```python
  s = "Hello@123!!世界"

  result = ''.join(
      c for c in s
      if ('A' <= c <= 'Z') or ('a' <= c <= 'z') or ('0' <= c <= '9')
  )

  print(result)  # Hello123
  ```

- 雙逼寫法
  ```python
  left = 0
  right = 0
  while left < right:
    ...
    if xxx:
        left += 1
    if xxx:
        right -= 1
  ```

# 概念補充

<str>.isalnum() -> 如果 <str> 是中文，也會被當成 True

"A".isalnum() # True
"z".isalnum() # True
"9".isalnum() # True
"@".isalnum() # False
" ".isalnum() # False

isalnum() 裡面的 alnum 是：
al = alphabet（字母）
num = number（數字）

| 方法        | 意思                 |
| ----------- | -------------------- |
| isalpha()   | 只字母               |
| isdigit()   | 只數字               |
| isnumeric() | 數字（包含全形數字） |
| isalnum()   | 字母或數字           |
| isascii()   | 是否為 ASCII         |
