class RecentCounter:

    def __init__(self):
        self._head = None
        self._size = 0

    def ping(self, t: int) -> int:
        if self._head == None:
            self._head = t
            self._size += 1
            return self._size
        elif self._head < t:
            self._head = t
            self._size += 1
            return self._size
        else:
            raise Error('t must be increasing')

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
