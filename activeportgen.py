# Let's imagine a scenario where we have a Server instance running different services such as http and ssh on different ports. Some of these services have an active state while others are inactive.

# class Server:

#     services = [
#         {'active': False, 'protocol': 'ftp', 'port': 21},
#         {'active': True, 'protocol': 'ssh', 'port': 22},
#         {'active': True, 'protocol': 'http', 'port': 80},
#     ]

# - Create a generator class that does the same thing

def nextactiveport(svc):
    start = 0
    active = []
    for x in svc:
        if x['active']:
            active.append(x)
    activelen = len(active)

    while start < activelen:
        yield active[start]
        start += 1

services = [
    {'active': False, 'protocol': 'ftp', 'port': 21},
    {'active': True, 'protocol': 'ssh', 'port': 22},
    {'active': True, 'protocol': 'http', 'port': 80},
]

a = nextactiveport(services)
print(next(a))
print(next(a))
print(next(a))