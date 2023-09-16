def file_status(file_path):
    try:
        with open(file_path, 'r') as file:
            print(f"a. Read Only: {file.readable()}")
            print(f"b. Closed: {file.closed}")
            print(f"c. Opening Mode: {file.mode}")
            print(f"d. File Name: {file.name}")
    except FileNotFoundError:
        print("File not found!")

file_path = 'myfile.txt'  
file_status(file_path)
