#import Numbers
#from Numbers import DisplayFactors
#from Numbers import *
import Numbers as NUM    #alise

def main():
    print("Enter the number:")
    No = int(input())
    
    #Numbers.DisplayFactors(No)
    NUM.DisplayFactors(No)
    
if __name__ == "__main__":
    main()