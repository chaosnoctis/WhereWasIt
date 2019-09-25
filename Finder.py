from pathlib import Path
import re

class Finder():
    """Class that maintains the current working directory(cwd) and searches within files for string queries"""
    def __init__(self):
        self._cwd: str = str(Path.cwd())

    def _validateSetter(self,value):
        path = Path(value)
        if value.startswith('~'):
            path = path.expanduser()
        if not path.exists():
            raise Exception("The path you specified does not exist.")
        if not path.is_dir():
            raise Exception("The path you specified must be a directory. Not a file")
        return path
    @property
    def cwd(self) -> str:
        return self._cwd
    
    @cwd.setter
    def cwd(self, value: str) -> None:
        """This is effectively the same as finding the directory specified"""
        if not isinstance(value, str):
            raise Exception("Please pass in valid argument")
        path = self._validateSetter(path)
        self._cwd = str(path.resolve())
    
    def list_files_cwd(self):
        """Obtain a list of the files in the current working directory and print them on the screen"""
        print(self.cwd)
        print('Files:\n')
        flist = [x for x in Path(self.cwd).iterdir() if x.is_file()]
        for num, files in enumerate(flist, 1):
            print(f"{num}. {files}")
        return flist
    
    def search_file_in_directory(self, pattern:str = None):
        """Given a pattern, it opens each files in the directory and prints out whether it found the string or not"""
        #Allow user to choose what file they want to open and store it in a
        # variable
        path = Path(self.cwd)
        while True:
            _file = input("What file do you want to open?\n> ")
            file_path = path.joinpath(_file)
            if file_path.is_file():
                break
            else:
                print("That is not a file in this directory. Please try again.\n\n")
        # Open the file and search of a pattern as specified in the function above
        # The statement below correctly returns whether the line contains the
        # pattern or not
        with open(f'{_file}', 'r') as f:
            if pattern is None:
                print('You did not specify a pattern, file closing...')
                f.close()
            if pattern in f.read():
                print('The string is in this file!')
            elif pattern not in f.read():
                print('Pattern was not found')
    def search_all_files(self,pattern=None):
    # Copy the list of files in the directory from the last function
    # Iterate over the list of files, opening and searching in each one until it gets a match
    # Similar to search specific file but more automated/looping
        rpattern = re.compile('{}'.format(pattern))

        flist = self.list_files_cwd()
        print('\nWe are going to scan these files now...')
        for num, i in enumerate(flist, 1):
            with i.open(encoding="latin-1") as f:
                if pattern is None:
                    print('You did not specify a pattern, file closing...')
                    f.close()
                if rpattern.search(f.read()):
                    print(num, i, 'The string is in this file!')
                else:
                    print(num, i, 'Pattern was not found')

if __name__ == "__main__":
    print('Don\'t run me directly, run main.py')