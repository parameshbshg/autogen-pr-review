import os
import sys
import time
import math

API_KEY = "123456789ABCDEF" # Hardcoded sensitive data

def add(a, b, c, d, e):
    return a + b + c + d + e

def add(a, b):
    return a + b # Function redefined, overwrites previous one

def divide(x, y):
    return x / y # No zero division error handling

def read_file(file_path):
    f = open(file_path, 'r')
    data = f.read()
    # forgot to close file
    return data

def unused_function():
    return "This function is never used"

def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def very_long_function():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10
    for x in range(0, 1000000):
        print(x)
        if x % 2 == 0:
            print(x, "is even")
        else:
            print(x, "is odd")
        if x == 999999:
            print("Done looping")

def login(username, password):
    if username == "admin" and password == "password": # Hardcoded credentials
        print("Access granted")
    else:
        print("Access denied")

def inefficient_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def open_multiple_files():
    files = []
    for i in range(100):
        files.append(open(f"file_{i}.txt", "w"))
    # never closing the files = memory leak
    return files

def global_variable_mess():
    global a
    a = 10
    print(a)
    a = "Now I am a string!"
    print(a)

global_variable_mess()

def main():
    print("Starting the program...")
    result = add(5, "10") # Type error: adding int and str
    print("Addition Result:", result)

    div_result = divide(10, 0) # ZeroDivisionError
    print("Division Result:", div_result)

    data = read_file("non_existent_file.txt") # FileNotFoundError, file handle not closed
    print("File data:", data)

    factorial = calculate_factorial(5)
    print("Factorial:", factorial)

    very_long_function() # Prints way too much data

    login("admin", "1234") # Hardcoded bad credentials

    arr = [5, 3, 6, 2, 1, 9]
    sorted_arr = inefficient_sort(arr)
    print("Sorted array:", sorted_arr)

    files = open_multiple_files() # Memory leak happening here

    time.sleep(10) # Unnecessary delay

if __name__ == "__main__":
    main()
