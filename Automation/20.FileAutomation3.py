import sys

def Addition(A,B):
    return A+B

def main():
    print("------------------------------------------")
    print("------Automation to perform Addition------")
    print("------------------------------------------")

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to perform addition of 2 integral values")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of the script: ")
            print("Name_Of_File First_Arguement Second_Arguement")
            print("Note: Both the arguements should be in the integral format")
            exit()
        
        else:
            print("Invalid option")
            print("Use --h option to get the help and use --u option to get the usage of application")
            exit()
        
    if(len(sys.argv) == 3):
        ret = Addition(int(sys.argv[1]), int(sys.argv[2]))
        print("Addition is: ",ret)

    else:
        print("Invalid option")
        print("Use --h option to get the help and use --u option to get the usage of application")
        print("------------------------------------------")
        print("------ty for using our script------")
        print("------------------------------------------")
        exit()
        
if __name__ == "__main__":
    main()