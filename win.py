import data

def addWin () :
    oldContents = data.getFileContents()
    newFile = open(data.filename, "w")
    w, l = oldContents.split("-")
    wins = int(w) + 1
    newContent = str(wins) + "-" + l
    newFile.write(newContent)
    newFile.close()

addWin()
