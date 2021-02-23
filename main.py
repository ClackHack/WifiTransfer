import socket,os,sys
from send import transfer
def main():
    args = sys.argv
    if len(args) == 1:
        #TODO Dynamic Path Choice
        pass
    elif len(args) == 2:
        if args[1].lower()=="recieve":
            pass
        else:
            transfer(path)
        #TODO Static Path Choice vs recieve
    else:
        print("Recieved too many or too few arguments...")
    input("Press 'Enter' to exit...\n")

if __name__=="__main__":
    main()