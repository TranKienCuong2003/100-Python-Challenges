class StringProcessor:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

def test_StringProcessor():
    processor = StringProcessor()
    processor.getString()
    processor.printString()

test_StringProcessor()
