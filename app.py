import logging

logging.basicConfig(
    
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d  %H:%M:%S',
    handlers=[
        logging.FileHandler('App1.log'),
        logging.StreamHandler()
    ]

)
logger=logging.getLogger("ArithmenticAPP")

def add(a,b): 

    res=a+b
    logger.debug(f"Adding {a} + {b}={res}")

    return res


def sub(a,b):
    res=a-b
    logger.debug(f"Subtracting {a} - {b}={res}")

    return res


def mul(a,b):
    res=a*b
    logger.debug(f"Multiplying {a} and {b}")
    return res

def div(a,b):
    try:
        res=a/b
        logger.debug(f"Dividing {a} and {b}")
        return res
    except ZeroDivisionError:
        logger.exception("Division by zero error ")
        return None
    



print(add(10,20))
print(sub(10,20))
print(mul(10,20))
print(div(10,20))
# print(div(10,0))

