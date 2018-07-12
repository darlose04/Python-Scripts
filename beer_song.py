def recite(start, take=1):

    beer = start

    while beer > 2:

        print("{} bottles of beer on the wall, {} bottles of beer. Take one down and pass it around, {} bottles of beer on the wall.".format(
            beer, beer, beer-1))
        beer -= 1

    if beer == 2:
        print("2 bottles of beer on the wall, 2 bottles of beer. Take one down and pass it around, 1 bottle of beer on the wall.")
        beer -= 1

        if beer == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer. Take it down and pass it around, no more bottles of beer on the wall.")

    return "No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, {} bottles of beer on the wall.".format(start)


print(recite(5, take=1))
