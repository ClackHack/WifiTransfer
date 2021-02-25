import socket,os
def receive(path):
    SEPERATOR=bytes('&*&*&*&*&*&*&','utf-8')
    SUBSEP=bytes('!@!@!@!@!@!@!','utf-8')
    sb = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sb.connect(("8.8.8.8", 80))
    ip = str(sb.getsockname()[0])
    sb.close()
    target = input("IP: ")
    port=5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    s.settimeout(10)
    #amount = s.recv(50).decode("utf-8")
    data = bytes("","utf-8")
    while 1:
        temp=s.recv(1000)
        if not temp:
            break
        data+=temp
    #print(data)
    d=data.split(SEPERATOR)
    amount=int(d[0].strip(bytes("AMOUNT:",'utf-8')))
    t=d[1].strip(bytes("FILES:",'utf-8')).split(SUBSEP)
    raw=d[2].strip(bytes("DATA:",'utf-8')).split(SUBSEP)
    for i in range(amount):
        if t[i] == bytes('RAW','utf-8'):
            print(raw[i].decode('utf-8'))
        else:
            #print(t[i],raw[i])
            try:
                 os.makedirs(os.path.dirname(t[i]), exist_ok=True)
            except Exception as e:
                print(e)
            finally:
                p=t[i].decode('utf-8')
                print(f"Writing to {p}")
                open(p,'wb').write(raw[i])
                
    '''print(amount)
    amount=int(amount)
    print(f"Writing {amount} objects")
    for i in range(amount):
        ty=s.recv(30).decode("utf-8")
        print(ty)
        data = bytes("","utf-8")
        while 1:
            temp=s.recv(1000)
            if not temp:
                break
            data+=temp
        print(data)
        if ty=="TEXT":
            print(data.decode("utf-8"))
        else:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            open(os.path.join(path,ty),"wb").write(data)'''

