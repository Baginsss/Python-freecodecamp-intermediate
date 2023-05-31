from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()

# Create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

# Start each processes
for p in processes:
    p.start()

# Join
for p in processes:
    p.join()

print('end main')

# something is wrong above here

threads = []
num_threads = 10


for i in range(num_threads):
    t = threads(target=square_numbers)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print('end main')

# later I need to retake this, cuz nothing works

