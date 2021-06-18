def number_of_bottles():
    lyrics = ""
    for i in range(6,-1,-1):
        if i == 0:
            lyrics += "No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall. \n"
        elif i == 1:
            lyrics += "1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall. \n"
        elif i == 2:
            lyrics += f"{i} bottles of milk on the wall, {i} bottles of milk. Take one down and pass it around, 1 more bottle of milk on the wall. \n"
        else:
            lyrics += f"{i} bottles of milk on the wall, {i} bottles of milk. Take one down and pass it around, {i-1} bottles of milk on the wall.\n"
    print(lyrics)

number_of_bottles()