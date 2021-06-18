# Your code here!!
def sing():
    lyrics = ""
    for i in range(9):
        if i == 4:
            lyrics += "whisper words of wisdom, let it be, let it be, \n"
        elif i == 8:
            lyrics += "there will be an answer, let it be"
        else:
            lyrics += "let it be, \n" 
    print(lyrics)

sing()

# let it be,
# let it be,
# let it be,
# let it be,
# whisper words of wisdom, let it be, let it be,
# let it be,
# let it be,
# let it be,
# there will be an answer, let it be