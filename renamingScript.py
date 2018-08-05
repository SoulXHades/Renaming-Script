import os

#fix filenames due to sorting order caused by lexicographic sorting
def fixing(files):
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
def renaming(files):
	#for file number
	i = 1

	#prompt for new file name
	newName = input("New name for your files: ")

	try:
		for file in files:
			os.rename(path + file, path + newName + str(i) + file[-4:])

			i += 1
	except Exception as e:
		print("Error: " + e)
	else:
		print("Renamed successfully!")



#get path of folder
path, quit = getFilePath()

#for main menu
while 1:
	#to exit if user wants to exit program
	if(quit):
		#clear screen (cross platform)
		os.system('cls' if os.name == 'nt' else 'clear')
		break

	#get a list of files in lexicographic order
	files = os.listdir(path)

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
		renaming(files)
		path, quit = getFilePath()
	elif(int(ans) == 2):
		fixing(files)
	elif(int(ans) == 3):
		quit = True
	else:
		#clear screen (cross platform)
		os.system('cls' if os.name == 'nt' else 'clear')

		print("Please the following options.")

