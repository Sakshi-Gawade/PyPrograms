

class Numbers:
    def __init__(self):   #Default constructor
        self.Size = 0
        self.Arr = list()   #self.Arr = []
        self.Accept()

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

    def Summation(self):
        Sum = 0
        for i in range(0,self.Size):
            Sum = Sum  + self.Arr[i]

        return Sum

    def Average(self):
        Sum = 0
        for i in range(0,self.Size):
            Sum = Sum  + self.Arr[i]

        return (Sum/self.Size)

    def Maximum(self):
        Max = self.Arr[0]
        for i in range(0,self.Size):
            if(self.Arr[i] > Max):
                Max = self.Arr[i]
        return Max

    def Minimum(self):
        Min = self.Arr[0]
        for i in range(0,self.Size):
            if(self.Arr[i] < Min):
                Min = self.Arr[i]
        return Min

def main():
    
    obj = Numbers()
    obj.Display()

    Output = obj.Summation()
    print("Addition of all elements:", Output)

    Output = obj.Average()
    print("Average of all elements:", Output)

    Output = obj.Maximum()
    print("Largest element is:", Output)

    Output = obj.Minimum()
    print("Smallest element is:", Output)

if __name__ == "__main__":
    main()