# 2. Let's imagine a scenario where we have a Server instance running different services such as http and ssh on different ports. Some of these services have an active state while others are inactive.

# class Server:

#     services = [
#         {'active': False, 'protocol': 'ftp', 'port': 21},
#         {'active': True, 'protocol': 'ssh', 'port': 22},
#         {'active': True, 'protocol': 'http', 'port': 80},
#     ]

# - Create an iterators for the Server class which would loop over only the active ports

class nextactiveport:
    def __init__(self):
        self.services = [
            {'active': False, 'protocol': 'ftp', 'port': 21},
            {'active': True, 'protocol': 'ssh', 'port': 22},
            {'active': True, 'protocol': 'http', 'port': 80},
        ]
        self.start = 0
    def __iter__(self):
        self.active = []
        for x in self.services:
            if x['active']:
                self.active.append(x)
        self.activelen = len(self.active)
        return self
    def __next__(self):
        if self.start < self.activelen:
            value = self.active[self.start]
            self.start += 1
            return value
        else:
            raise StopIteration

a = nextactiveport()
aPort = iter(a)
print(next(aPort))
print(next(aPort))
print(next(aPort))