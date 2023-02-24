import sys

def main():
    print("DEmonstration of Command Line Arguments")

    print("Name of application:",sys.argv[0])

    x = int(sys.argv[1])

    y = int(sys.argv[2])

    z = x + y

    print(z)

if __name__ == "__main__":
    main()