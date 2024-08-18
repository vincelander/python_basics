"""
    DEBUG: Detailed information, typically of interest only when diagnosing problems.
    INFO: Confirmation that things are working as expected.
    WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
    ERROR: Due to a more serious problem, the software has not been able to perform some function.
    CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
"""
import logging

# if logging.basucConfig is not defined or it is define with filename param, nothing will display in terminal
logging.basicConfig(
    filename='./Logging Basics/calc_logs.log',
    level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s',
)

def add(x, y):
    """"Addition Function"""
    return x + y

def subtract(x, y):
    """"Subtraction Function"""
    return x - y

def multiply(x, y):
    """"Muliplication Function"""
    return x * y

def devide(x, y):
    """"Division Function"""
    if y == 0:
        raise ValueError('Cannot devide by zero.')
    return x / y        # using double / (//) mean four devision means doesn't look for remainder

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logging.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.info('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.info('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

dev_result = devide(num_1, num_2)
logging.info('Dev: {} / {} = {}'.format(num_1, num_2, dev_result))