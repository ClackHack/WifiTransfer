import socket,os,sys
from send import transfer
from receive import recieve
def main():
    args = sys.argv
    print(sys.argv)
    path = os.path.dirname(sys.argv[0])
    print(path)
    if len(args) == 1:

        transfer(input("Path: ").replace('\\',"/"))
    elif len(args) == 2:
        if args[1].lower()=="receive":
            recieve(path)
        else:
            transfer(args[1])
    else:
        print("Received too many or too few arguments...")
    #input("Press 'Enter' to exit...\n")

if __name__=="__main__":
    main()