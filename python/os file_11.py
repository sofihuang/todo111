import os
import shutil # for copy file , delete directory

path = "C:\\Users\\huang\\OneDrive\\桌面\\python"
path2 = "src/python/test.txt" #relative path!!

print("******************* detect if path exists *******************")

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")

print("******************* read file *******************")

try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file is not found")

print("******************* write file *******************")

text = "Hi\nHow's going\nHope you have a nice day!"

with open('test.txt','w') as file: #'r' means read , 'a' means append, 'w' overwrite
    file.write(text)


with open('test.txt','a') as file: 
    file.write("\nNice to meet you XD")

print("******************* copy file *******************")
#copyfile:copies contents of a file
#copy():copyfile()+permission mode + destination can be a directory
#copy2():copy()+copies metadata(file's creation and modification times)

shutil.copyfile('test.txt','copy.txt') #src ,dst
#shutil.copy('test.txt','copy.txt')
#shutil.copy2('test.txt','copy.txt')
# you cant write the directory which you want to the copy in , in the example the copy is loated in the same folder

print("******************* move file *******************")

source = "test.txt"
destination = "C:\\Users\\huang\\OneDrive\\桌面\\prueba\\text.txt" # at last ypu need to add source name unless the file can't be added

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+ " was moved")
except FileNotFoundError:
    print(source+" was not found")

print("******************* delete file *******************")

path3 = "copy.txt"

try:
    os.remove(path3) #delete file
    # os.rmdir(path3) # delete empty directory
    # shutil.rmtree(path3) #delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have permission to delete the file ")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path + " was deleted")