import os 
import multiprocessing

def SumFactors(No):
    Sum = 0
    for i in range(1, int((No/2)+1)):
        if(No % i == 0):
            Sum = Sum + i
    return Sum

def CheckPerfect(No):
    Ans = SumFactors(No)

    if(No == Ans):
        return True
    else:
        return False

def main():
    print("Enter the number :")
    #Value = 0
    Value = int(input())

    pobj = multiprocessing.Pool()

    Ret = pobj.map(CheckPerfect, Value)

    if(Ret == True):
        print("Number is Prime")
    else:
        print("Number is not prime")

if __name__ == "__main__":
    main()