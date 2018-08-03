#this is a basic program that renames all .jpg files with a new name with a number starting from 1
import os

def sorting(files):
	#for file number
	i = 1

	try:
		for file in files:
			os.rename(path + file, path + newName + str(i) + ".jpg")

			i += 1
	except Exception as e:
		print("Error: " + e)



#prompt for directory which contains all the files
path = input("Input directory:\n") + "\\"

#get a list of files in lexicographic order
files = os.listdir(path)

#prompt for new file name
newName = input("New name for your files: ")

#show user the sequence of the items in the list
print(files)

ans = input("sort? Y/N\n").lower()

if(ans == "y"):
	sorting(files)