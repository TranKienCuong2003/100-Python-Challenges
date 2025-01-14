def throws():
    return 5 / 0

try:
    throws()
except ZeroDivisionError:
    print("division by zero!")
except Exception as err:
    print(f'Caught an exception: {err}')
finally:
    print('In finally block for cleanup')
