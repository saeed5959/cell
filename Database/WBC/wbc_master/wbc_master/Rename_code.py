import os
dir = "./Lamphosit/"
#method which handle all the operation regarding rename the file.
def rename_files():
    #variable initialization
    i=0
    for file_name in os.listdir(dir):
        dstination="l-" + str(i) + ".jpg"
        print(dstination)
        sourse=dir+ file_name
        print(sourse)
        dstination=dir+ dstination
        print(dstination)
        #rename function calls to rename the files.
        os.rename(sourse, dstination)
        #variable increment to differenciate the all files like newname1.html
        #,newname2.html ..... so on.
        i += 1
    print("All files has been renamed successfully...")    
#rename_files method call.
rename_files()