from multiprocessing import Process
from multiprocessing import Lock
import os

def sum(x,y,lock):
    with lock:
        sum = x+y
        print("Sum: " + str(sum))

def quo(x,y,lock):
    with lock:
        z = x/y
        print("Quotient: " + str(z))

def dif(x,y,lock):
    with lock:
        z = x-y
        print("Difference: " + str(z))

def prod(x,y,lock):
    with lock:
        z = x*y
        print("Product: " + str(z))

if __name__ == '__main__':
        

    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))

    Processes = [Process(target= sum,args = (x,y,Lock())),Process(target= quo,args = (x,y,Lock())),Process(target= dif,args = (x,y,Lock())),Process(target= prod,args = (x,y,Lock()))]

    for process in Processes:
        process.start()

    for process in Processes:
        process.join()


    print("We are done.")
