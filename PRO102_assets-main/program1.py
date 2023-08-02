import os
import shutil
from_dir = "/Users/lindasabei/Downloads/C102_assets-main"
to_dir = "/Users/lindasabei/Downloads/C102_assets-main/sorted"
listOfFiles = os.listdir(from_dir)
print(listOfFiles) 
for fileName in listOfFiles:
    name,extension = os.path.splitext(fileName)
    if extension == "":
        continue
    if extension in [".gif",".png",".jpg",".jpeg",".jfif"]:
        path1 = from_dir+"/"+fileName
        path2 = to_dir+"/"+"imageFiles"
        path3 = to_dir+"/"+"imageFiles"+"/"+fileName
        
        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
            
        else:
            os.makedirs(path2)
            print("moving")
            shutil.move(path1,path3)