import zlib

original_string = "hello world!hello world!hello world!hello world!"

compressed_string = zlib.compress(original_string.encode('utf-8'))
print(f"Compressed String: {compressed_string}")

decompressed_string = zlib.decompress(compressed_string).decode('utf-8')
print(f"Decompressed String: {decompressed_string}")
