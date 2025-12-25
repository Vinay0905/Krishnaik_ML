
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

import time 

def format_number(number):
    time.sleep(1)
    return f"Number: {number}"

def sqaure_number(number):
    time.sleep(1)
    return f"Square: {number*number}"

numbers = [1,2,3,4,5,6,7,8,9,10,1,2,3]

# with ThreadPoolExecutor(max_workers=3) as executor:
#     results = executor.map(format_number, numbers)

# for result in results:
#     print(result)

if __name__=="__main__":
    
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(sqaure_number, numbers)

    for result in results:
        print(result)