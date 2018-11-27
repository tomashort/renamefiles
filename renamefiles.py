import os

def rename_files(dir):
    # Set current working directory
    os.chdir(dir)

    # Get file names from folder
    file_list = os.listdir(dir)
    
    # Rename each file
    for file_name in file_list:
        new_name = file_name.translate(file_name.maketrans('', '', '0123456789'))
        if not new_name == file_name:
            os.rename(file_name, new_name)
            print(f"Renamed {file_name} to {new_name}")
    
rename_files(r"C:\Users\Tom\Documents\Code\Udacity\Python\secretmessage")
