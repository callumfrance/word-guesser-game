words = list()

def import_words(fileName):
    # Import the 9-letter words into the program's memory from the word list
    with open(fileName) as fo:
        for line in fo:
            temp = line.rstrip()
            if(len(temp) == 9):
                words.append(temp)


def export_words(outFilName):
    with open(outFilName, "w+") as fo:
        for x in words:
            fo.write(x + "\n")


if __name__ == '__main__':
    fileName = input('\nInput >')
    import_words(fileName)
    outFilName = input('\nOutput >')
    export_words(outFilName)
