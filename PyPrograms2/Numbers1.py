

class Numbers:
    def __init__(self):
        self.Size = 0
        self.Arr = list()   #self.Arr = []

    def Accept(self):
        print("How many elements you want :")
        self.Size = int(input())

        print("Please Enter the elements :")
        Value = 0
        for i in range(0,self.Size):
            Value = int(input())
            self.Arr.append(Value)

    def Display(self):
        print("Elements from list are :")
        for i in range(0, self.Size):
            print(self.Arr[i])

def main():
    
    obj = Numbers()
    obj.Accept()
    obj.Display()

if __name__ == "__main__":
    main()