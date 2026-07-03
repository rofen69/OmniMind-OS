"""
Memory Manager

Temporary in-memory storage.
Will later be upgraded to persistent memory.
"""


class Memory:
    """Simple key-value memory."""

    def __init__(self):
        self._storage = {}

    def store(self, key: str, value):
        self._storage[key] = value

    def retrieve(self, key: str):
        return self._storage.get(key)

    def delete(self, key: str):
        self._storage.pop(key, None)

    def clear(self):
        self._storage.clear()