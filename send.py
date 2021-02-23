import socket,os

def send(path,conn,base,raw=False):
    ty=""
    if not raw:
        try:
            data=open(path,"rb",encoding="utf-8").read()
            ty=path.strip(base)
        except:
            print(f"Unable to read file {path}")
            return
    else:
        ty="TEXT"
        data = bytes(path,"utf-8")
    conn.sendall(data)
def transfer(path,base):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = str(s.getsockname()[0])
    s.close()
    HOST = ip
    PORT=5000
    s.listen(1)
    print(f"Enter {HOST} on client to initiate transfer")
    conn,addr=s.accept()
    if os.isdir(path):
        paths = []
        for p,d,f in os.walk(path):
            paths.extend(f)
        for i in paths:
            conn.sendall(bytes(str(len(paths)),"utf-8"))
            send(i,conn,base)
    elif os.isfile(path):
        conn.sendall(bytes(str(1), "utf-8"))
        send(i,base,conn)
    else:
        conn.sendall(bytes(str(1), "utf-8"))
        send(path,conn,base,raw=True)
