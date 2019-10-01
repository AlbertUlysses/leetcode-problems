class RecentCounter(object):

    def __init__(self):
        self.counter = []

    def ping(self, t):
        self.counter.insert(0,t)
        while t-3000>self.counter[len(self.counter)-1]:
            self.counter.pop()
        return len(self.counterlass RecentCounter:
