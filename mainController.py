def changeDirectory(finder):
    response = input("Enter the desired directory path:")
    try:
        finder.cwd = response
        print("Successfully set! " + finder.cwd)
        return True
    except:
        return False
def search_file_in_directory(finder):
    confirmation = input(f'CWD: {finder.cwd} \nIs this right?[y/N] ')
    if confirmation[0].lower() == 'y':
        pattern = input('What is the string you\'d like to search? ')
        finder.list_files_cwd()
        finder.search_file_in_directory(pattern)
    elif confirmation[0].lower() =='n':
        chdir_resp = input('Would you like to change directories? [y/N] ')
        if chdir_resp[0].lower() == 'y':
            if(changeDirectory(finder)):
                search_file_in_directory(finder)
def search_all_files_in_cwd(finder):
    pattern = input("What is the string you\'d like to search? ")
    try:
        finder.search_all_files(pattern)
        return True
    except:
        return False

if __name__ == "__main__":
    print('Don\'t run me directly, run main.py')