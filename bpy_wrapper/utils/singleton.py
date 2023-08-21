from typing import Any, Dict


class Singleton(type):
    _instances: Dict['Singleton', 'Singleton'] = {}

    def __call__(self, *args: Any, **kwargs: Any) -> 'Singleton':
        if self not in self._instances:
            self._instances[self] = super(Singleton, self).__call__(*args, **kwargs)
        return self._instances[self]
