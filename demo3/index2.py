# 集合，查询速度最快，union、difference、
# 示例二：使用集合去重，或者找共同的元素，或者合并集合

values = set('aeeouiaerere')

values_another = set('xxxey')

concat_value = values.union(values_another) # 合并两个集合

diff_value = values.difference(values_another) # 包含在values中，但是不包含在values_another中

inter_value = values.intersection(values_another) # 两个集合的共同元素

print(concat_value)
print(diff_value)
print(inter_value)
