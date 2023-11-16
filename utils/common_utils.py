def singleton_instance(cls):
    """装饰器单例模式初始化实例"""
    instance = {}

    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return get_instance
