# 使用类来创建《上下文管理器》


class UserData:
    def __init__(self, data: dict)->None:
        self.init_data = data

    def __enter__(self):
        self.end_data = self.init_data
        return self.end_data

    def __exit__(self, exc_type, exc_value, exc_trace):
        self.end_data
