import socket

SERVER_IP = '192.168.137.1'
SERVER_PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT))
    while True:
        username = input("Please enter your name")
        PassWord = input("Please enter your password")
        Type = input('enter L for Login or S for SignUp')
        data = f"{username}:{PassWord}:{Type}".encode()
        s.sendall(data)
        response = s.recv(1024)

        if response == b'YOU ARE AUTHORISED':

            print("WELCOME")
        elif response == b'YOU ARE NOT AUTHORISED':

            print('ACCESS DENIED')


        elif response == b'SUCCESS':
            print("SIGNED UP SUCCESSFULLY")

        elif response == b'Username NOT FOUND':
            print("USERNAME NOT FOUND")

        elif response == b'username is taken':
            print('USERNAME NOT AVAILABLE')
            continue


