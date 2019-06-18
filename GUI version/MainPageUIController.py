import os


class MainPageUIController(object):
    def __init__(self):
        super().__init__()

    # return 0s to add to current filename's number to make sure end results of all filenames of the same length
    # private method
    def __additionOfZeros(self, currentFileNum, totalNumOfFiles):
        # default is empty incase don't require adding of 0s
        self.zeros = ""
        self.sizeOfCurrentFileNum = self.sizeOfTotalFilesNum = 10

        # to get the number of digits in the number that is going to be assigned to the current filename
        currentFileNum //= 10

        while currentFileNum != 0:
            currentFileNum //= 10
            self.sizeOfCurrentFileNum *= 10

        # to get the number of digits in the number that is going to be assigned to the final filename (max number of digits setting as standard)
        totalNumOfFiles //= 10
        while totalNumOfFiles != 0:
            totalNumOfFiles //= 10
            self.sizeOfTotalFilesNum *= 10

        # to obtain the number of digits off
        self.zeros = str(self.sizeOfTotalFilesNum // self.sizeOfCurrentFileNum)

        # remove the '1' from 10 or 100, etc
        return self.zeros.strip("1")

    # fix filenames due to sorting order caused by lexicographic sorting
    def fixing(self, path):
        # if error is True, error messages will not be cleared
        self.success = True
        self.files = os.listdir(path)   # get a list of files from that folder
        self.maximum = self.__getLongestFileNameLen(self.files)

        while 1:
            # to exit infinite WHILE loop if all file in files are fixed
            self.exit = True
            # get a list of files in lexicographic order
            self.files = os.listdir(path)

            try:
                for self.file in self.files:
                    # lengthen current filename if not equals to the length of the longest filename in the list
                    if len(self.file) != self.maximum:
                        os.rename(path + self.file, path + "0" + self.file)
                        self.exit = False
                        break
            except Exception as e:
                print("Error: " + e)
                self.success = False

            # exit function if all file in files are fixed
            if self.exit:
                return self.success  # return to boundary so boundary will know if there is an error or not

    # get list of sorted file names from that directory
    def getFiles(self, path):
        # get a list of files in lexicographic order
        self.files = os.listdir(path)
        # arrange files in ascending order
        self.files.sort()

        return self.files

    # get the length of the longest filename
    # private method
    def __getLongestFileNameLen(self, files):
        self.maximum = 0

        for self.file in self.files:
            if len(self.file) > self.maximum:
                self.maximum = len(self.file)

        return self.maximum

    # rename all the files with the same name and ascending number at the back
    def renaming(self, path, newName, filesList=[]):
        # for file number
        self.i = 1

        if len(filesList) == 0:
            self.files = self.getFiles(path)    # get list of file names from that folder
        else:
            self.files = filesList
        # to use to know how many 0s to add to current file depend on num of files
        self.totalNumOfFiles = len(self.files)

        try:
            for self.file in self.files:
                self.filePathToWrite = path + newName + self.__additionOfZeros(self.i, self.totalNumOfFiles) \
                                       + str(self.i) + self.file[-4:];

                # check if filename exist as the exception doesn't catch by Try Except
                if os.path.exists(self.filePathToWrite):
                    # rename the remaining files in another name (one unicode largers) so no conflict
                    self.renaming(path=path, newName=newName[:-1] + chr(ord(newName[-1]) + 1),
                                  filesList=self.files[self.i - 1:])
                    # rename back the user wanted file name.
                    self.renaming(path=path, newName=newName)
                    break
                else:
                    os.rename(path + self.file, path + newName + self.__additionOfZeros(self.i, self.totalNumOfFiles) + str(self.i) + self.file[-4:])

                self.i += 1
        except Exception as e:
            print("Error: " + str(e))
            return False
        else:
            # have return value so that if recurence function call occurs,
            # won't have many print("Renamed successfully!") if put that in this function
            return True
