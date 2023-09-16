file_path = 'myfile.txt'  

with open(file_path, 'w') as file:
    user_input = input("Enter text to store in the file: ")
    file.write(user_input)
