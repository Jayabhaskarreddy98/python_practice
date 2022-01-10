# reading from file
file = ('C:\\Users\\VIJAY BHASKAR\\Jaya\\jaya\\file_handling\\sample1.txt')
handle = open(file)
# getting key to search
key = input('Enter the word you want : ')
# writting into a file
file = ('C:\\Users\\VIJAY BHASKAR\\Jaya\\jaya\\file_handling\\demo.txt')
handle1 = open(file, 'a')
# actual operation
handle1.write(f'\n This is the new output \n')
for line in handle:
    handle1.write(f"'{key}' is present in '{line}', '{key in line}'")

handle.close()
handle1.close()    