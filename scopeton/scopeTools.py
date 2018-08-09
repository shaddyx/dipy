def getBeanName(cls):
    if isinstance(cls, str):
        return cls
    from scopeton.objects import Bean
    if isinstance(cls, Bean):
        return cls.name
    return cls.__name__

def callMethodByName(obj, name, *args, **kwargs):
    if hasattr(obj, name):
        return getattr(obj, name)(*args, **kwargs)


class ScopetonException(Exception):
    def __init__(self, *args, **kwargs):
        super(Exception, self).__init__(*args, **kwargs)