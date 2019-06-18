import os

#return 0s to add to current filename's number to make sure end results of all filenames of the same length
def additionOfZeros(currentFileNum, totalNumOfFiles):
	#default is empty incase don't require adding of 0s
	zeros = ""
	sizeOfCurrentFileNum = sizeOfTotalFilesNum = 10

	#to get the number of digits in the number that is going to be assigned to the current filename
	currentFileNum //= 10

	while currentFileNum != 0:
		currentFileNum //= 10
		sizeOfCurrentFileNum *= 10

	#to get the number of digits in the number that is going to be assigned to the final filename (max number of digits setting as standard)
	totalNumOfFiles //= 10
	while totalNumOfFiles != 0:
		totalNumOfFiles //= 10
		sizeOfTotalFilesNum *= 10


	#to obtain the number of digits off
	zeros = str(sizeOfTotalFilesNum // sizeOfCurrentFileNum)

	#remove the '1' from 10 or 100, etc
	return zeros.strip("1")


#fix filenames due to sorting order caused by lexicographic sorting
def fixing(files):
	#if error is True, error messages will not be cleared
	error = False
	maximum = getLongestFileNameLen(files)

	while 1:
		#to exit infinite WHILE loop if all file in files are fixed
		exit = True
		#get a list of files in lexicographic order
		files = os.listdir(path)

		try:
			for file in files:
				#lengthen current filename if not equals to the length of the longest filename in the list
				if(len(file) != maximum):
					os.rename(path + file, path + "0" + file)
					exit = False
					break
		except Exception as e:
			print("Error: " + e)
			error = True

		#exit function if all file in files are fixed
		if(exit):
			#so as to not clear away Exception message if there is
			if(not(error)):
				#clear screen (cross platform)
				os.system('cls' if os.name == 'nt' else 'clear')

			return


#get list of sorted file names from that directory
def getFiles(path):
	#get a list of files in lexicographic order
	files = os.listdir(path)
	#arrange files in ascending order
	files.sort()

	return files


#get the directory path
def getFilePath():
	#prompt for directory which contains all the files
	path = input("Input directory (Q to quit):\n") + "\\"

	#clear screen (cross platform)
	os.system('cls' if os.name == 'nt' else 'clear')

	if(path[0].lower() != 'q'):
		return path, False

	return path, True


#get the length of the longest filename
def getLongestFileNameLen(files):
	maximum = 0

	for file in files:
		if(len(file) > maximum):
			maximum = len(file)

	return maximum


#rename all the files with the same name and ascending number at the back
def renaming(files, newName):
	#for file number
	i = 1
	#to use to know how many 0s to add to current file depend on num of files
	totalNumOfFiles = len(files)

	try:
		for file in files:
			filePathToWrite = path + newName + additionOfZeros(i, totalNumOfFiles) + str(i) + file[-4:];

			#check if filename exist as the exception doesn't catch by Try Except
			if os.path.exists(filePathToWrite):
				#rename the remaining files in another name (one unicode largers) so no conflict
				renaming(files[i-1:], newName[:-1] + chr(ord(newName[-1])+1))
				#rename back the user wanted file name. Need getFiles() to get new list of new file names in the directory
				renaming(getFiles(path), newName)
				break
			else:
				os.rename(path + file, path + newName + additionOfZeros(i, totalNumOfFiles) + str(i) + file[-4:])

			i += 1
	except Exception as e:
		print("Error: " + str(e))
		return 0
	else:
		#have return value so that if recurence function call occurs, 
		#won't have many print("Renamed successfully!") if put that in this function
		return 1



#get path of folder
path, quit = getFilePath()

#for main menu
while 1:
	#to exit if user wants to exit program
	if(quit):
		#clear screen (cross platform)
		os.system('cls' if os.name == 'nt' else 'clear')
		break

	#get list of sorted file names from that directory
	files = getFiles(path)

	#show user the sequence of the items in the list
	print(files)


	#main menu
	print("\n1. Rename \
		\nRename all the files with a same new name but numbers at the back in ascending order.")
	print("2. Fix file names \
		\nFix the file names by adding 0s if is now sorted in ascending order due to lexicographic issue.")
	print("3. Quit")

	ans = input("Input option here: ")

	if(not(ans.isdigit())):
		#clear screen (cross platform)
		os.system('cls' if os.name == 'nt' else 'clear')

		print("Please input numbers only.")
	elif(int(ans) == 1):
		#prompt for new file name
		newName = input("New name for your files: ")
		if(renaming(files, newName)):
			print("Renamed successfully!") 
		path, quit = getFilePath()
	elif(int(ans) == 2):
		fixing(files)
	elif(int(ans) == 3):
		quit = True
	else:
		#clear screen (cross platform)
		os.system('cls' if os.name == 'nt' else 'clear')

		print("Please the following options.")

