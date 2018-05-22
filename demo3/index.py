# 字典，不会维持插入顺序
# 示例一：记录输入的元音字母的频度
values = ['a', 'e', 'i', 'o', 'u']
founds = {}
# for item in values:
#     founds[item] = 0

isBegin = True

while(isBegin):
    word = input("you can input a word:(input y to end!)")

    if word == 'y' or word == 'Y':
        isBegin = False
    else:
        for item in word:
            if item in values:
                founds.setdefault(item, 0) # 调用python自带的设置默认值的API
                founds[item] += 1
                
for k, v in sorted(founds.items()):
    print(k, 'was found', v, 'time')
