# Application to find out the maximum number.

def Maximum(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2

def main():
    print("Enter First number")
    Value1 = input()

    print("enter second number")
    Value2 = input()

    Ret = Maximum(int(Value1), int(Value2))  #positional parameter/argumemt

    print("Largest number is:",Ret)

if __name__ == "__main__":
    main()