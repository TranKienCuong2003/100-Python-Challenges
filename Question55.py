def raise_runtime_error():
    raise RuntimeError("This is a RuntimeError exception")

try:
    raise_runtime_error()
except RuntimeError as e:
    print(f"Caught an exception: {e}")
