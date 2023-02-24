import os

def DeleteFile(FileName):
    if(os.path.exists(FileName)):
        os.remove(FileName)
        print("File is successfully deleted!!")
    else:
        print("There is no such file")

def main():
    print("Enter the file name to delete ")
    Name = input()

    DeleteFile(Name)

if __name__ == "__main__":
    main()