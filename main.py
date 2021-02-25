import socket,os,sys
from send import transfer
from receive import receive
import gui
def main():
    args = sys.argv
    #print(sys.argv)
    path = os.path.dirname(sys.argv[0])
    #print(path)
    if len(args) == 1:
        main = gui.main()
        main.mainloop()
    elif len(args) == 2:
        if args[1].lower()=="receive":
            receive(path)
        else:
            transfer(args[1],path)
    else:
        if args[1].lower()=="raw":
            transfer(" ".join(args[2:]),path,raw=True)
        else:
            print("Received too many or too few arguments...")
    #input("Press 'Enter' to exit...\n")

if __name__=="__main__":
    main()
