class FileManager:
    def __init__(self, fileName):
        self.fileName = fileName

    def writeData(self, textContent):
        fileObj = open(self.fileName, "w")
        fileObj.write(textContent)
        fileObj.close()
        print("Data written successfully.")

    def readData(self):
        fileObj = open(self.fileName, "r")
        fileContent = fileObj.read()
        fileObj.close()
        print("File Content:")
        print(fileContent)


fileHandler = FileManager("records.txt")
fileHandler.writeData("Roll No: 101\nName: Ankit Sharma\nBranch: CSE")
fileHandler.readData()
