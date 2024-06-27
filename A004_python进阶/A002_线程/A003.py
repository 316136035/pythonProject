import threading
import random
import time

threading.local()
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        super().__init__()
        
    def run(self):
        print("Starting " + self.name)


if __name__ == "__main__":
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Exiting Main Thread")