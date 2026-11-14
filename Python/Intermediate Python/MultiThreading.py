# Intermediate Python Course | Class 12. MultiThreading
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Creating a thread
# -----------------------------------------------------------------------

import threading
import time

def worker():
    print("Worker started")
    time.sleep(2)
    print("Worker finished")

t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)

t1.start()
t2.start()

t1.join()
t2.join()

print("Main finished")

# ----------------------------------------------------------------------
# B. Passing arguments to threads
# ----------------------------------------------------------------------

import threading
import time

def worker(seconds, name):
    print(f"{name} started")
    time.sleep(seconds)
    print(f"{name} finished")

t1 = threading.Thread(target=worker, args=(2, "Thread 1"))
t2 = threading.Thread(target=worker, args=(3, "Thread 2"))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done")

# -----------------------------------------------------------------------
# D. Sharing data between threads
# -----------------------------------------------------------------------

import threading

database = []

def add_data(value):
    database.append(value)

threads = []

for i in range(5):
    t = threading.Thread(target=add_data, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(database)

# -----------------------------------------------------------------------
# E. Daemon threads
# -----------------------------------------------------------------------

import threading
import time

def background_task():
    while True:
        print("Background task running")
        time.sleep(1)

t = threading.Thread(target=background_task, daemon=True)
t.start()

time.sleep(3)
print("Main program finished")

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------