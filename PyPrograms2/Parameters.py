#Positional Arguments
def Add1(No1, No2):
    print("value of No1 :", No1)
    print("value of No1 :", No2)
    return No1 + No2

def Sub1(No1, No2):
    print("value of No1 :", No1)
    print("value of No1 :", No2)
    return No1 - No2

def Div1(No1, No2):
    print("value of No1 :", No1)
    print("value of No1 :", No2)
    return No1 / No2


def main():
    Ans = 0
    Ans = Add1(10, 11)
    print("Addition is:", Ans)

    Ans = Sub1(No2 = 10,No1 = 11)
    print("Substraction is:", Ans)

    Ans = Sub1(No1 = 10,No2 = 11)
    print("Substraction is:", Ans)

    Ans = Div1(No1 = 10,No2 = 2)
    print("Division is:", Ans)

    Ans = Div1(No1 = 2,No2 = 10)
    print("Division is:", Ans)

if __name__ == "__main__":
    main()