import os.path

filename = "output.txt"

def getFileContents():
    if os.path.isfile(filename):
        readFile = open(filename, "r")
        contents = readFile.read()
        readFile.close()
        return contents
    else:
        defaultScore = "0-0"
        newFile = open(filename, "w")
        newFile.write(defaultScore)
        newFile.close()
        return defaultScore
