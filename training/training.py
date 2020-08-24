f = open("file.txt", mode="a")

f.write("Bye World")
f.close()

f= open("file.txt", "r")

output = f.read()

print(output)

f.close()


