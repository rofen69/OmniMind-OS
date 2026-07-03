"""
Session Memory

Stores temporary state for a user session.
"""


class SessionMemory:
    """Lightweight session storage."""

    def __init__(self):
        self._data = {}

    def set(self, key: str, value):
        self._data[key] = value

    def get(self, key: str):
        return self._data.get(key)

    def reset(self):
        self._data.clear()