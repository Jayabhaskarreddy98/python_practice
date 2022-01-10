file = ('C:\\Users\\VIJAY BHASKAR\\Jaya\\jaya\\file_handling\\sample1.txt')

handle = open(file)
key = input('Enter the word we want : ')

for line in handle:
    print(f"'{key}' is present in '{line}' {key in line}")
