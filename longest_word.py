def longest(string):
    arr = string.split()
    print(max(arr, key=len))

longest("The quick brown fox jumped over the fence")