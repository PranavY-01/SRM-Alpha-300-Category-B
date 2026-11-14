# Intermediate Python Course | Class 13. Multiprocessing
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# A. Creating a process
# -----------------------------------------------------------------------

import multiprocessing
import time

def worker():
    print("Worker started")
    time.sleep(2)
    print("Worker finished")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=worker)
    p2 = multiprocessing.Process(target=worker)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Main finished")

# ----------------------------------------------------------------------
# B. Passing arguments to processes
# ----------------------------------------------------------------------

from multiprocessing import Process, Value, Lock
import time

def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        number.value += 1
        lock.release()

if __name__ == "__main__":

    lock = Lock()
    shared_number = Value('i', 0)

    print('Number at beginning is', shared_number.value)

    p1 = Process(target=add_100, args=(shared_number, lock))
    p2 = Process(target=add_100, args=(shared_number, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Number at end is', shared_number.value)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------