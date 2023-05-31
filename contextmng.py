# Context managers are used to manage resources, such as files, sockets, and locks.

with open('notes.txt', 'w') as file:
    file.write('Some todo...')

file = open('notes.txt', 'w')
try:
    file.write('Some todo...')
finally:
    file.close()

from threading import Lock
lock = Lock()

lock.acquire()
# thread safe operations
lock.release()

class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()

with ManagedFile('notes.txt') as file:
    print('some todo...')
    file.write('Some todo...')

