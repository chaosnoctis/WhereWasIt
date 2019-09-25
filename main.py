from Finder import Finder
import mainController
print("Name: WhereWasIt.py")
print("Author: Christian Arty")
print("Description: An application that allows you to open a file and search for a specific string within the file. Additionally, it can recursively search entire directory for the strings")
print("Repo: https://github.com/christianarty/WhereWasIt")
print("#####################################################################")
print("#####################################################################")

finder = Finder()
commands = ["Search a file in this directory", "Search for a string within all the files in this directory","Change your directory"]
print(f"Your current directory is: {finder.cwd}")
print("Would you like to: ")
for num, command in enumerate(commands, 1):
    print(f"{num}. {command}")

response = input(f'[Please enter between 1-{len(commands)}] >')

# Error handling
if not response.isdigit():
    raise Exception("Please enter a valid integer")
response = int(response)
if (response < 0 or response > len(commands)):
    raise Exception("Please enter a number that is within the range")

options={
    1:mainController.search_file_in_directory,
    2:mainController.search_all_files_in_cwd,
    3:mainController.changeDirectory
}
#TODO: Check if the response has been true or false
options[response](finder)




