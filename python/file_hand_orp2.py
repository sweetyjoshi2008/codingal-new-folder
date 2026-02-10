#create a new file
new_file = open('New_File.txt', 'x')
new_file.close()

#check if a file exists
import os
print("Checking if my_file exists or not....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

#create a new if it doesn't
my_file = open("my_file.txt", "w")
my_file.write("hy i am vansh , i am 2year old ")
my_file.close()

#delete file named codingal
os.remove('C:\\Users\\SWEETY JOSHI\\OneDrive\Desktop\\codingal new folder\\python\\Codingal.txt')

#delete the folder
os.rmdir('Folder')