import socket
import secrets
import hashlib

SERVER_IP = '192.168.137.1'
SERVER_PORT = 5678
UsersData = []
flag = False
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))

    print('Server is listening')
    s.listen(1)
    conn, addr = s.accept()
    print(f'Connection accepted from :{addr}')
    with conn:
        while True:

            #conn.send(b'Hello World')
            data = conn.recv(1024)
            UserDetails = data.decode().split(':')

            MessageType = UserDetails[2]
            username = UserDetails[0]
            PassWord = UserDetails[1]

            if MessageType == 'S' or MessageType == 's':
                for UserName in UsersData:
                    if UserData[0] == username:
                        conn.send(b'username is taken')
                        break
                token_hex = secrets.token_hex(16)
                mal7 = bytes.fromhex(token_hex)
                saltedPass = PassWord.encode() + mal7
                HashedPass = hashlib.sha512(saltedPass).hexdigest()
                userDeets = [username, PassWord, saltedPass, HashedPass, mal7]


                UsersData.append(userDeets)
                print(userDeets)
                print("User signed up successfully")
                conn.send(b'SUCCESS')
                # print(HashedPass)
            elif MessageType == 'l' or MessageType == 'L':

                for UserData in UsersData:

                    if UserData[0] == username:
                        flag = True
                        salt = UserData[4]
                        salted = PassWord.encode() + salt
                        hashed = hashlib.sha512(salted).hexdigest()
                        if UserData[3] == hashed:
                            conn.send(b'YOU ARE AUTHORISED')
                            print('A')
                            break
                        elif UserData[3] != hashed:
                            conn.send(b'YOU ARE NOT AUTHORISED')
                            print('NA')
                            break

                if flag == False:
                    conn.send(b'Username NOT FOUND')


