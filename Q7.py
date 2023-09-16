import keyword

def count_python_keywords(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()
        keywords = keyword.kwlist
        count = sum(1 for word in source_code.split() if word in keywords)
        print(f"Number of Python keywords: {count}")

python_source_file = 'example.py'  # Replace with your Python source file path
count_python_keywords(python_source_file)
