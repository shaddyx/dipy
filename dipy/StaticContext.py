import copy
from threading import RLock

from dipy import DiTools
from dipy.ContextBean import ContextBean

lock = RLock()
def _StaticSync(fn):
    def wrapped(*args, **kwargs):
        lock.acquire()
        try:
            return fn(*args, **kwargs)
        finally:
            lock.release()
    return wrapped


class StaticContext(object):
    _beans = {}  # type: dict[str, object]
    @classmethod
    @_StaticSync
    def getBeansCopy(cls):
        return copy.copy(cls._beans)

    @classmethod
    @_StaticSync
    def registerBean(cls, clazz):
        # type: (str, ContextBean) -> object
        bean = ContextBean()
        bean.name = DiTools.getFullyQualifiedName(clazz)
        bean.object = clazz
        cls._beans[bean.name] = bean

def Service():
    def decorator(cls):
        StaticContext.registerBean(cls)
        return cls
    return decorator