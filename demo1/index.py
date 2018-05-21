# python数组去重
print("python数组去重")
num = [1,2,3,2,4]
new_num = []

for item in num:
    if item not in new_num:
        new_num.append(item)
print(new_num)