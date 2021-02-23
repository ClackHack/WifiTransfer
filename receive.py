import socket,os
def receive(path):
    sb = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sb.connect(("8.8.8.8", 80))
    ip = str(sb.getsockname()[0])
    sb.close()
    target = input("IP: ")
    port=5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    s.settimeout(1)
    amount = int(s.recv(50).decode("utf-8"))
    print(f"Writing {amount} objects")
    for i in range(amount):
        ty=s.recv(30).decode("utf-8")

        data = bytes("","utf-8")
        while 1:
            temp=s.recv(1000)
            if not temp:
                break
            data+=temp
        if ty=="TEXT":
            print(data.decode("utf-8"))
        else:
            open(ty,"wb").write(data)

