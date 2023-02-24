#Instance variable : Name, Amount, Address, AccountNo
#Instance method : CreateAccount(), DiaplayAccountInfo
class Bank_Account:

    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your name :")
        self.Name = input()

        print("Enter your initial Amount :")
        self.Amount = int(input())

        print("Enter your address :")
        self.Address = input()

        print("Enter your Account Number :")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("-----------Your Account information is as below ------------")
        print("Name of Account Holder :", self.Name)
        print("Account Number :", self.AccountNo)
        print("Address of Account Holder :", self.Address)
        print("Current amount in account :", self.Amount)

def main():
    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating the First account")
    User1.CreateAccount()

    print("Creating the Second account")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

if __name__ == "__main__":
    main()