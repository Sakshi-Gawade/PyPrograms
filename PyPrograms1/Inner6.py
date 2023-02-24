
def Division(A,B):
    Ans = 0
    Ans = A / B
    return Ans

def Decorated_Function(Function_Name):
    def Inner(A,B):
        if(A < B):
            A,B = B,A
        return Function_Name(A,B)
    return Inner

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number :"))

    New_Function = Decorated_Function(Division)
    ret = New_Function(Value1,Value2)
    print("Substraction is:",ret)


if __name__ == "__main__":
    main()