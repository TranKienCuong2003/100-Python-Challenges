class MyError(Exception):
    """My own exception class

    Attributes:
        msg -- explanation of the error
    """
    
    def __init__(self, msg):
        self.msg = msg

try:
    raise MyError("something wrong")
except MyError as e:
    print(f"Caught MyError: {e.msg}")
