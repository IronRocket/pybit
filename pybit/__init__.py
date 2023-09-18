class bitarray:
    def __init__(self,arr=()) -> None:
        self.data = arr
    def appendbits(self, bits:tuple) -> None:
        """Appends tuple bools to raw tuple"""
        self.data = self.data+tuple([bit for bit in bits if str(type(bit)) == "<class \'bool\'>"])
    def core_data(self) -> tuple:
        """Returns core tuple"""
        return self.data

    def pop(self,index:int) -> bool:
        """Converts core tuple to list and pops (index)\n
        Converts core list back into core tuple
        """
        mutable = list(self.data)
        poped_item = mutable.pop(index)
        self.data = tuple(mutable)
        return poped_item



def str_binary_to_bool(string:str) -> tuple:
    """Converts "101" -> (True,False,True)"""
    binary = []
    for char in string:
        if char == "1":
            binary.append(True)
        elif char == "0":
            binary.append(False)
        else:
            raise Exception(f"Expected binary(1,0) got {char}")
    return tuple(binary)

def bool_to_str_binary(bits:tuple) -> str:
    """Convert (True,False,True) -> "101" """
    str_binary = ""
    for bit in bits:
        if bit == True:
            str_binary += "1"
        elif bit == False:
            str_binary += "0"
        else:
            raise Exception(f"Expected bool got {bit}")


def decimal_to_binary(decimal:int) -> tuple:
    """Convert 256 -> (False, False, False, False, False, False, False)"""
    binary = []
    while decimal/2 > 1:
        decimal = decimal/2
        
        if str(decimal)[-1] != "0":
            binary.append(True)
        else:
            binary.append(False)

    return tuple(binary)

def binary_to_decimal(bits:tuple) -> tuple:
    """Convert tuple binary to decimal"""
    decimal = 0
    length = len(bits)-1
    for bit in bits:
        if bit:
            decimal += 2**length
        length -= 1
    return decimal

def binary_to_hex(bits:tuple) -> str:
    """Convert (False,True,False) -> 0x1\n
    Alternatives:
        hex(pybit.binary_to_decimal((False,True,False)))
    """
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
    str_hex = ''
    scope = []
    for bit in bits:
        scope.append(bit)
        count += 1
        if count == 4:
            count = 0
            str_hex += conversion_table[tuple(scope)]
            scope = []
    return str_hex



__author__ = "IronRocket"
__license__= "MIT"
__source__ = "https://github.com/pybit-binary/pybit"
__version__ = "1"