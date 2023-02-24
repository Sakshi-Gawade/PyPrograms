# Accept elements from the user and insert it into the list

def main():
    Arr = list()  #creating empty list  or object of list

    print("Enter how many elements you want to store:")
    size = int(input())

    print("Please enter the values:") 

    for i in range(0, size):
        no = int(input())
        Arr.append(no) #Arr.insert(i, no)

    print(Arr)

if __name__ == "__main__":
    main()