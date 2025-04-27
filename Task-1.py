try:
    file1 = open("sample.txt", 'r')
    writing_files = file1.read()
    print(writing_files)
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
