
def Display(No):
    
    if(No > 0):
        No = No - 1
        Display(No)   # Head recursion
        print(No)

Display(4)