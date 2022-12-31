import pybit


#Conversions

#str -> bool_tuple
print("String -> Bool_tuple:",pybit.str_binary_to_bool("1010"))

#bool_tuple -> str
print("Bool_tuple -> string:",pybit.bool_to_str_binary((True,False,True,True)))

#binary -> decimal
print("Binary -> Decimal:",pybit.binary_to_decimal("1010"))

#decimal -> binary
print("Decimal -> Binary",pybit.decimal_to_binary(10))

#Binary -> Hex
print("Binary -> Hex",pybit.binary_to_hex("1010"))
#--------------------------------------------------------------------------------


#Bitarrays

x = pybit.bitarray()


x.appendbits((True,False))

print("Tuple containing two bits:",x.raw_data())