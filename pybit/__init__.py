class bitarray:
    def __init__(self) -> None:
        self.data = []
    def appendbits(self, bits:tuple) -> None:
        for bit in bits:
            if str(type(bit)) == "<class \'bool\'>":
                self.data.append(bit)
            else:
                raise Exception("Expected boolean got {bit}")        
    def raw_data(self) -> tuple:
        return self.data 



def str_binary_to_bool(string:str) -> tuple:
    binary = []
    for char in string:
        if char == "1":
            binary.append(True)
        elif char == "0":
            binary.append(False)
        else:
            raise Exception("Expected binary(1,0) got {bit}")
    return tuple(binary)

def decimal_to_binary(decimal:int) -> tuple:
    binary = []
    while decimal/2 > 1:
        decimal = decimal/2
        
        if str(decimal)[-1] != "0":
            binary.append(True)
        else:
            binary.append(False)

    return tuple(binary)

def binary_to_decimal(bits:tuple) -> tuple:
    decimal = 0
    length = len(bits)-1
    for bit in bits:
        if bit == True:
            decimal += 2**length
        length -= 1
    return decimal

def binary_to_hex(bits:tuple) -> str:
    conversion_table = {
        (False, False, False, False):"0",
        (False, False, False, True):"1",
        (False, False, True, False):"2",
        (False, False, True, True):"3",
        (False, True, False, False):"4",
        (False, True, False, True):"5",
        (False, True, True, False):"6",
        (False, True, True, True):"7",
        (True, False, False, False):"8",
        (True, False, False, True):"9",
        (True, False, True, False):"a",
        (True, False, True, True):"b",
        (True, True, False, False):"c",
        (True, True, False, True):"d",
        (True, True, True, False):"e",
        (True, True, True, True):"f"
    }
    count = 0
    hex = ""
    scope = []
    for bit in bits:
        scope.append(bit)
        count += 1

        if count == 4:
            count = 0
            hex += conversion_table[tuple(scope)]
            scope = []
    return hex



__author__ = "IronRocket"
__license__= "MIT"
__source__ = "https://github.com/pybit-binary/pybit"
__version__ = "1"