# Binary to Decimal and Back Converter
# Develop a converter to convert a decimal number to binary
# or a binary number to its decimal equivalent

def bin_converter():

    decimal = float(input('Please enter a number: '))
    convert = bin(int(decimal))
    print(convert)

bin_converter()
