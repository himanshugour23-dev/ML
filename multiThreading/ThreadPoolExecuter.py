##multithreeading with thread pole executor 

from concurrent.futures import ThreadPoolExecutor
import time

def show_number(number):
    time.sleep(1)
    print(f"Number: {number}")

numbers = [1,2,3,4,5]

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(show_number, numbers)