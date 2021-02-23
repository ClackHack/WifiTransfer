import socket,os

def send(path,conn,raw=False):
    if not raw:
        try:
            data=open(path,"rb").read()
        except:
            print(f"Unable to read file {path}")
    else:
        data = bytes(path,"utf-8")
    conn.sendall(data)
def transfer(path):
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
            send(i,conn)
    elif os.isfile(path):
        send(i,conn)
    else:
        send(path,conn,raw=True)
