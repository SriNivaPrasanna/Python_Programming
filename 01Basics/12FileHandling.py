'''
File Handling -> to store the data

Text file -> .txt , .py, .html

Binary File -> mp3, mp4, png, jpg 


modes: 
r -> read mode -> It opens the file only if it is already existing
w ->  write mode
a -> append mode

rb
wb
'''

file = open("./11functions.py" , "r")
#print(file)

#print(file.read())
#print(file.readlines()[0])

#print(file.readline())
#print(file.readline())
#print(file.readline())

#for data in file:
#     print(data, end="")

#print(file.read(5))
#print(file.seek(10))
#print(file.read(5))
#file.close()

#file = open("./temp.txt" , "w")
#file.write("I am writing ")
#file.write("Hey, there")
#file.close()

#file = open("./temp.txt" , "a")
#file.write("I am writing ")
#file.write("Hey, there")
#file.close()

#with open("./temp.txt", "r") as f1:
#     print(f1.read())

#print("It closes the file")


#with open("./11functions.py","r") as f1 , open("./copy.txt","w") as f2:
#     for data in f1:
#         f2.write(data)


#with open("../python.jpg" , "rb") as f1 , open("../copy.jpg" , "wb") as f2:
#    print(f1.read())
#for data in f1:
#        f2.write(data)