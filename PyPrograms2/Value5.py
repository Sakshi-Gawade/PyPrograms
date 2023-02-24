#Accept One number from user and check whether it is it is prime or not 
class Value:

    def __init__(self,Data):   #parametrised constructor
        self.No = Data

    def SumFactors(self):
        Sum = 0

        for i in range(2, int((self.No/2)+1)):
            if(self.No % i == 0):
                Sum = Sum + i

        return Sum

    def CheckPrime(self):
        i = 0
        Flag = True

        for i in range(2, int(self.No/2)+1):
            if(self.No % i == 0):
                Flag = False
                break

        return Flag
       

def main():
    print("Please enter number :")
    A = int(input())

    obj = Value(A)

    Ret = obj.CheckPrime()
    if(Ret == True):
        print("{} is prime number".format(A))
    else:
        print("{} is not prime number".format(A))

if __name__ == "__main__":
    main()