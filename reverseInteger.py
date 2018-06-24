def reverse(x):

    intString = str(x)
    lstString = list(intString)

    if lstString[0] == '-':
        lstString.pop(0)
        return int('-' + ''.join(lstString[::-1]))

    else:
        return int(''.join(lstString[::-1]))
    
    


print(reverse(-10235))
