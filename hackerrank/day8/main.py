# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def main():
    
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    
    n = int(input_data[0])
    
    
    phone_book = {}
    
    
    index = 1
    
   
    for _ in range(n):
        name = input_data[index]
        phone = input_data[index + 1]
        phone_book[name] = phone
        index += 2
        
   
    while index < len(input_data):
        query_name = input_data[index]
        
        
        if query_name in phone_book:
            print(f"{query_name}={phone_book[query_name]}")
        else:
            print("Not found")
            