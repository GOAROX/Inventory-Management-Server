import socket
from helper import delete, sorted, create_string, updated

HOST = '192.168.1.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # set up the server
    s.bind((HOST, PORT))
    s.listen()
    # connection is established
    conn, addr = s.accept()
    with conn: 
        print('Connected by', addr)
        while True:
            # wait for data
            data = conn.recv(1024).decode()
            if not data:
                break
            # Parse the request
            lines = data.split('\n')
            if lines[0].strip() == 'Request':
                # handle request
                line2 = lines[1].split()
                message_type = line2[0]
                if message_type == 'Sorted':
                    if line2[1] == 'Name':
                        print('Sorting by name')
                        file_text = create_string(sorted(0))
                        print('i get here')
                        response = 'Response\ndata\n' + file_text
                        print(response)
                        conn.sendall(response.encode())
                    elif line2[1] == 'Quantity':
                        print('Sorting by quantity')
                        file_text = create_string(sorted(1))
                        response = 'Response\ndata\n' + file_text
                        conn.sendall(response.encode())
                    elif line2[1] == 'Date':
                        print('Sorting by date')
                        file_text = create_string(sorted(2))
                        response = 'Response\ndata\n' + file_text
                        print(file_text)
                        conn.sendall(response.encode())
                    else:
                        response = 'Response\nerror\nInvalid data field for Sorted: ' + line2[1]
                        conn.sendall(response.encode())

                elif message_type == 'Update':
                    print("Entered update")
                    name = line2[1]
                    newq = line2[2]
                    print(name + " " + newq)
                    msg = updated(name, newq)
                    conn.sendall(msg.encode())

                elif message_type == "Delete":
                    print("Entered delete")
                    name = line2[1]
                    print(name)
                    msg = delete(name)
                    conn.sendall(msg.encode())

            else:
                conn.sendall(('Error, uknown message: ' + lines[0]).encode())
            


