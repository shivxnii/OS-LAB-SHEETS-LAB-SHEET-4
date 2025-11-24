#task2
from multiprocessing import Process, freeze_support
import logging
import time

logging.basicConfig(filename='system_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(processName)s - %(message)s')

def process_task(name):
    print(f"{name} started")   # terminal output
    logging.info(f"{name} started")
    time.sleep(2)
    print(f"{name} terminated")
    logging.info(f"{name} terminated")

if __name__ == '__main__':
    freeze_support()

    print("System Booting...")

    p1 = Process(target=process_task, args=("Process-1",))
    p2 = Process(target=process_task, args=("Process-2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("System Shutdown.")
