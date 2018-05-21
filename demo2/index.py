# 列表切片(start, end, step)
str = "Don't panic"
arr = list(str)
arr1 = []
print(arr[-4:-6:-1])
arr1.extend(arr[1:3])
arr1.extend([' '])
arr1.extend([''.join(arr[4])])
arr1.extend(arr[-4:-6:-1])
print(''.join(arr1))

# 列表方法：insert、remove、pop、extend等，具有破坏性
# 切片不会改变列表状态