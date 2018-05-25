# 类的示例
class ToIncreament:
    def __init__(self, v: int=0, i: int=1) ->None:
        self.v = v
        self.i = i
    def __repr__(self)->str:
        # 覆盖默认对象的返回格式为字符串形式 
        return str(self.v)

    def increament(self)->None:
        self.v += self.i


value = ToIncreament()
print(value)
value.increament()
print(value)
