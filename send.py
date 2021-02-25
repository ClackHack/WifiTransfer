import socket,os

def transfer(path,base,raw=False,log=None):
    if not log:
        log=print
    SEPERATOR="&*&*&*&*&*&*&"
    SUBSEP="!@!@!@!@!@!@!"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = str(s.getsockname()[0])
    s.close()
    HOST = ip
    PORT=5000
    #log("Gon connect")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind((HOST,PORT))
    s.listen(1)
    log(f"Enter {HOST} on client to initiate transfer")
    #print(path,base)
    base=base.replace("\\",'/')
    conn,addr=s.accept()
    
    if raw:
        log("Sending raw text")
        conn.sendall(bytes("AMOUNT"+str(1),"utf-8"))
        conn.sendall(bytes(SEPERATOR+"FILES:RAW","utf-8"))
        conn.sendall(bytes(SEPERATOR+"DATA:"+path,"utf-8"))
        #send(path,conn,base,raw=True)
        return
    full=os.path.join(base,path).replace("\\","/")
    if os.path.isdir(path):
        print("Base: ",base)
        paths = []
        for p,d,f in os.walk(full):
            #print(p,d,f)
            #for ff in f:
                #print(os.path.join(p,ff).replace("\\",'/'))
                #print(os.path.join(p,ff).replace("\\",'/').replace(base,""))
                #print("\n")
            paths.extend([os.path.join(p,ff).replace("\\",'/').strip("/") for ff in f])
        #print(paths)
        conn.sendall(bytes("AMOUNT:"+str(len(paths)),"utf-8"))
        #print([ff.replace(base,"").strip("/") for ff in paths])
        conn.sendall(bytes(SEPERATOR+"FILES:"+SUBSEP.join([ff.replace(base,"").strip("/") for ff in paths]),"utf-8"))
        conn.sendall(bytes(SEPERATOR+"DATA:","utf-8")+bytes(SUBSEP,"utf-8").join([open(i,"rb").read() for i in paths]))
        #for i in paths:
            
            #send(i,conn,base)
    #elif os.path.exists(full):
    else:
        log("Sending File")
        conn.sendall(bytes("AMOUNT"+str(1),"utf-8"))
        conn.sendall(bytes(SEPERATOR+"FILES:"+path,"utf-8"))
        conn.sendall(bytes(SEPERATOR+"DATA:","utf-8")+open(full,"rb").read())
        #send(i,conn,base)
    log("Successfully sent all files")
    '''else:
        print(path,full,os.path.isfile(full))'''
