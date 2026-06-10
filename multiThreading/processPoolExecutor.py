##multiprocessor 

from concurrent.futures import ProcessPoolExecutor
import time

def show_number(number):
    time.sleep(1)
    return number * number

numbers = [1,2,3,4,5,6]

if __name__ == "__main__":
     ## pool executor works with what fn writerns not with run 
    with ProcessPoolExecutor(max_workers=3) as executor:
        result = executor.map(show_number, numbers)

    for res in result:
        print(res)