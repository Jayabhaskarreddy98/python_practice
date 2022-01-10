file = ('C:\\Users\\VIJAY BHASKAR\\Jaya\\jaya\\file_handling\\demo.txt')

handle = open(file, 'w')
key = input('Enter the word we want : ')

handle.write(key)
handle.flush()