# read file
file = open('data.txt')
data = file.read()
file.close()

# write file
out = open('data2.txt', 'w')
out.write(data)
out.close()
