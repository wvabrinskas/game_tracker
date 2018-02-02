import os.path

filename = os.getcwd() + "/output.txt"
defaultScore = "0-0"

def getFileContents():
    if os.path.isfile(filename):
        readFile = open(filename, "r")
        contents = readFile.read()
        readFile.close()
        return contents
    else:
        newFile = open(filename, "w")
        newFile.write(defaultScore)
        newFile.close()
        return defaultScore


def reset():
    readFile = open(filename, "w")
    readFile.write(defaultScore)
    readFile.close()
