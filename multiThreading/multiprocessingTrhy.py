##Multiprocessing allows to use process in parallel 
##CPU Bound Tasks 

import multiprocessing
import time 

def square():
    for i in range(5):
        time.sleep(1)
        print(f"Square {i*i} done")

def cube():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube {i*i*i} done")

if __name__ == "__main__":
    ##Create two proccess 
    p1=multiprocessing.Process(target=square)
    p2=multiprocessing.Process(target=cube)
    t = time.time()
    ## start the process 
    p1.start()
    p2.start()
    ## waiting for process to complete 
    p1.join()
    p2.join()

    print(time.time()-t)