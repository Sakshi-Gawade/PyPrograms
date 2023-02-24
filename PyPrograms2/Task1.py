import schedule
import time
import datetime
import sys 

def Fun():
    print("Inside Fun")

def main():
    print("Inside task schedular")

    schedule.every(1).minute.do(Fun)

    while(True):   # unconditional infinite loop
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()