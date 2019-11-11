def find_palandrome(value):
    string = str(value)
    length = len(string)
    palandrome = True
    for x in range (0, int((length / 2) + 1)):
        if string[x] == string[length-1-x]:
            palandrome == True
        else:
            palandrome = False
            break
    if palandrome == True:
        print("This is a palandrome")
    else:
        print("This is not a palandrome")

find_palandrome(1234321)

