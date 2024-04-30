import os
import sys

def get_directory():
    '''
    Description: Prompt user to enter directory name as a command-line argument.
    Returns: Directory name entered by user.
    '''
    try:
        return sys.argv[1]
    except IndexError:
        return 'Enter directory name!'

def get_files_dict(directory):
    '''
    Description: Create a dictionary with file extensions as keys and lists of corresponding files as values.
    Parameters:
        directory: Directory path.
    Returns: Dictionary containing files categorized by extensions.
    '''
    files_dict = {}
    for file_name in os.listdir(directory):
        file_ext = os.path.splitext(file_name)[1][1:]  # Get file extension
        if file_ext:  # Exclude directories
            files_dict.setdefault(file_ext, []).append(file_name)
    return files_dict

def main():
    '''
    Description: Main function to organize files in a directory by extension.
    '''
    directory = get_directory()
    if directory == 'Enter directory name!':
        print(directory)
    else:
        files_dict = get_files_dict(directory)
        print(files_dict)

if __name__ == "__main__":
    main()
