handle = open('C:\\Users\\VIJAY BHASKAR\\Jaya\\jaya\\file_handling\\sample.txt')
print(handle.read())

# for sentence in handle:
#     print(sentence, end='')
print(handle.tell())
handle.seek(0)
data = handle.readline()
while data:
    print(data)
    data = handle.readline(10)  