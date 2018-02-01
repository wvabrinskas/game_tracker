import data

def addWin () :
    oldContents = data.getFileContents()
    newFile = open(data.filename, "w")
    w, l = oldContents.split("-")
    loss = int(l) + 1
    newContent = w + "-" + str(loss)
    newFile.write(newContent)
    newFile.close()

addWin()
